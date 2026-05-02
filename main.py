import os
import gradio as gr
import numpy as np
from dotenv import load_dotenv
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
from google import genai


# CONFIG API

load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

if not API_KEY:
    raise ValueError("Falta GENAI_API_KEY")

client = genai.Client(api_key=API_KEY)


# MODELO EMBEDDINGS

embed_model = SentenceTransformer('all-MiniLM-L6-v2')


# VARIABLES GLOBALES

chunks = []
index = None


# SYSTEM PROMPT

SYSTEM_PROMPT = """
Eres un Tutor Socrático experto en Bases de Datos.

Reglas:
- No des respuestas directas
- Usa pistas y preguntas
- Usa SOLO el contexto proporcionado
"""

# LEER PDF

def load_pdf(file):
    reader = PdfReader(file.name)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    return text


# CHUNKING

def chunk_text(text, chunk_size=150, overlap=30):
    words = text.split()
    result = []

    start = 0
    while start < len(words):
        chunk = " ".join(words[start:start + chunk_size])
        result.append(chunk)
        start += chunk_size - overlap

    return result


# CREAR VECTOR STORE

def process_pdf(file):

    global chunks, index

    text = load_pdf(file)
    chunks = chunk_text(text)

    embeddings = embed_model.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return f" PDF procesado: {len(chunks)} chunks creados"


# RETRIEVE

def retrieve(query, k=3):

    global index, chunks

    if index is None:
        return "No hay datos cargados."

    query_vec = embed_model.encode([query])
    distances, indices = index.search(query_vec, k)

    results = [chunks[i] for i in indices[0]]
    return "\n".join(results)


# CHAT

def chat(user_input, history):

    context = retrieve(user_input)

    prompt = f"""
{SYSTEM_PROMPT}

<context>
{context}
</context>

<question>
{user_input}
</question>
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        reply = response.text

    except Exception as e:
        reply = f"Error: {str(e)}"

    return reply


# INTERFAZ

with gr.Blocks() as demo:

    gr.Markdown("# 🤖 RAG Tutor con PDFs")

    file_input = gr.File(label="Sube tu PDF")
    status = gr.Textbox(label="Estado")

    load_btn = gr.Button("Procesar PDF")

    chatbot = gr.ChatInterface(fn=chat)

    load_btn.click(fn=process_pdf, inputs=file_input, outputs=status)


# RUN

if __name__ == "__main__":
    demo.launch()
