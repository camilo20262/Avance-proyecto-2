# 🤖 Asistente Experto basado en RAG para Bases de Datos

## 📌 Descripción

Este proyecto implementa un **Asistente Inteligente basado en RAG (Retrieval-Augmented Generation)** que permite responder preguntas a partir de documentos proporcionados por el usuario (PDFs).

El sistema está diseñado como un **Tutor Socrático de Bases de Datos**, guiando al estudiante mediante pistas y preguntas en lugar de dar respuestas directas.

Funciona completamente de manera local en cuanto al procesamiento de documentos, preservando la privacidad de la información.

---

## 🎯 Objetivo

Desarrollar un sistema capaz de:

* Leer documentos PDF como base de conocimiento
* Procesar y fragmentar el contenido (chunking)
* Convertir texto en embeddings
* Almacenar información en una base vectorial (FAISS)
* Recuperar información relevante según la consulta
* Generar respuestas contextualizadas usando un modelo LLM

---

## 🧠 Arquitectura del Sistema (RAG)

El sistema implementa el siguiente flujo:

1. Carga de documento PDF
2. Extracción de texto
3. División en fragmentos (*chunks*)
4. Generación de embeddings (Sentence Transformers)
5. Almacenamiento en base vectorial (FAISS)
6. Consulta del usuario
7. Búsqueda semántica de los fragmentos más relevantes
8. Construcción del prompt con contexto
9. Generación de respuesta usando Gemini

---

## 🔄 Flujo del sistema

```
PDF → Texto → Chunks → Embeddings → FAISS
                                          ↓
Usuario → Pregunta → Embedding → Búsqueda
                                          ↓
Contexto relevante → Prompt → LLM → Respuesta
```

---

## ⚙️ Tecnologías utilizadas

* Python
* Gradio (interfaz web)
* Sentence Transformers (embeddings)
* FAISS (búsqueda vectorial)
* PyPDF (lectura de documentos)
* Google Gemini (modelo LLM)

---

## 🧩 Estructuración del Prompt

El sistema utiliza ingeniería de prompts para controlar el comportamiento del modelo:

### 🔹 System Prompt

Define el rol del asistente:

* Tutor socrático
* No responde directamente
* Usa preguntas guiadas
* Utiliza solo el contexto

---

### 🔹 Delimitadores

Se utilizan etiquetas para estructurar el prompt:

```text
<context>
...
</context>

<question>
...
</question>
```

---

### 🔹 Formato de salida

Las respuestas siguen una estructura en Markdown:

* **Pista:** explicación breve
* **Pregunta guía:** ayuda al razonamiento

---

## 📂 Estructura del proyecto

```
rag-asistente/
│
├── main.py
├── requirements.txt
├── .env
├── data/
│   └── documentos.pdf
└── docs/
    └── informe.pdf
```

---

## 🚀 Instalación y ejecución

### 1. Clonar repositorio

```bash
git clone <TU_REPOSITORIO>
cd rag-asistente
```

---

### 2. Crear entorno virtual

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Configurar API KEY

Crear archivo `.env`:

```env
GENAI_API_KEY=tu_api_key_aqui
```

---

### 5. Ejecutar aplicación

```bash
python main.py
```

Luego abrir en el navegador:

```
http://127.0.0.1:7860
```

---

## 🖥️ Uso del sistema

1. Subir un documento PDF
2. Presionar "Procesar PDF"
3. Realizar preguntas en el chat
4. Recibir respuestas guiadas basadas en el documento

---

## 📊 Ejemplo de uso

**Pregunta:**

```
¿Qué es una clave primaria?
```

**Respuesta:**

```
Pista:
Se utiliza para identificar registros únicos dentro de una tabla.

Pregunta guía:
¿Qué característica debería tener un atributo para identificar un registro sin repetirse?
```

---

## ⚠️ Consideraciones

* Si el PDF no contiene texto (escaneado), puede fallar la extracción
* El sistema responde únicamente en base al contexto recuperado
* Se incluye validación para evitar respuestas fuera del documento

---

## 📌 Resultados

El sistema permite:

* Consultar documentos de forma inteligente
* Aprender de manera guiada
* Reducir el uso de respuestas genéricas del modelo

---

## 👨‍💻 Autor

Proyecto académico - Ingeniería de Sistemas

---
