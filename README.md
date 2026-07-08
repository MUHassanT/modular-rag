# RAG-Based Database Schema Assistant

A modular Retrieval-Augmented Generation (RAG) application that answers natural language questions about a customer database schema stored in an Excel file.

The project reads the Excel file, converts each database field into a searchable document, generates semantic embeddings, stores them in a FAISS vector database, retrieves the most relevant information for a user's query, and uses a locally running Qwen model through Ollama to generate accurate responses.

---

## Features

- Read database schema from an Excel file using Pandas
- Convert every database field into a LangChain `Document`
- Modular RAG pipeline with each stage in a separate file
- Generate semantic embeddings using Sentence Transformers
- Store embeddings in a FAISS vector database
- Retrieve relevant information using vector similarity search
- Generate answers using the Qwen 3 language model through Ollama
- Simple command-line chatbot interface

---

## Project Structure

```
RAG/
│
├── data/
│   └── Copy of Customer.xlsx
│
├── src/
│   ├── read_excel.py
│   ├── chunk_documents.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

# RAG Pipeline

```
Excel File
     │
     ▼
Read Excel
     │
     ▼
Create Documents
     │
     ▼
Chunk Documents
     │
     ▼
Generate Embeddings
     │
     ▼
Build FAISS Vector Store
     │
     ▼
Retrieve Relevant Chunks
     │
     ▼
Generate Response using Qwen
     │
     ▼
Answer
```

---

# Project Modules

### `read_excel.py`

Reads the Excel file using Pandas and converts each row into a LangChain `Document`.

### `chunk_documents.py`

Splits documents into chunks using `RecursiveCharacterTextSplitter`.

Although each Excel row already represents one logical chunk, the chunking stage is retained to keep the RAG pipeline modular and to support larger document types in the future.

### `embeddings.py`

Generates vector embeddings using the `all-MiniLM-L6-v2` Sentence Transformer model.

### `vector_store.py`

Stores embeddings inside a FAISS vector database for efficient similarity search.

### `retriever.py`

Converts the user's question into an embedding, searches the FAISS index, and retrieves the most relevant document chunks.

### `llm.py`

Builds the prompt using the retrieved context and generates the final response using the Qwen 3 language model running locally through Ollama.

### `main.py`

Connects every stage of the RAG pipeline and provides a simple command-line interface.

---

# Technologies Used

- Python
- Pandas
- LangChain Core
- LangChain Text Splitters
- Sentence Transformers
- FAISS
- Ollama
- Qwen 3
- NumPy

---

# Why Pandas Instead of Unstructured?

Initially, the project used LangChain's `UnstructuredLoader` to read the Excel file.

However, `UnstructuredLoader` converts Excel spreadsheets into HTML-like tables, which caused multiple database fields to be grouped together inside the same chunk. This reduced retrieval accuracy because unrelated schema fields were embedded together.

Since the dataset was already structured, Pandas was used instead.

Each row in the Excel file represents a single database column, making it a natural unit of information. Using Pandas allowed each row to be converted into an individual LangChain `Document`, producing cleaner embeddings and more accurate retrieval.

---

# Chunking Strategy

This project uses **row-based chunking**.

Instead of splitting text by character count alone, each row of the Excel file is treated as one logical document because every row represents a single database field.

`RecursiveCharacterTextSplitter` is still included to maintain a modular RAG pipeline and to support future use with larger or unstructured documents.

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
cd RAG
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download Ollama:

https://ollama.com/download

Pull the Qwen model.

```bash
ollama pull qwen3:8b
```

For systems with limited GPU memory, `qwen3:4b` can also be used.

---

# Running the Project

```bash
python src/main.py
```

Example:

```
Ask a question:
What is MARITAL_STATUS?
```

Example response:

```
MARITAL_STATUS stores the customer's marital status.
It has the data type CHAR(1 BYTE) and is used where required to interpret related fields such as SPOUSE_NAME.
```

---

# Example Questions

- What is CUSTOMER_ID?
- What is MARITAL_STATUS?
- What is the data type of TAX_GROUP?
- Which field stores spouse information?
- Which field indicates customer residency?
- Explain CUSTOMER_CLASS.
- What does OCCUPATION represent?

---

# Future Improvements

- Save and reload the FAISS index instead of rebuilding it on every startup.
- Support additional document formats such as PDF and Word.
- Implement hybrid retrieval (vector search + keyword search).
- Build a web interface using Streamlit or Gradio.
- Add support for multiple knowledge bases.
- Improve prompt engineering for domain-specific responses.

---

# Learning Outcomes

This project demonstrates the complete Retrieval-Augmented Generation workflow:

- Reading structured data
- Document creation
- Chunking strategies
- Semantic embeddings
- Vector databases
- Similarity search
- Prompt engineering
- Local LLM inference using Ollama
- End-to-end modular RAG architecture

---

# License

This project was developed as part of an internship to understand the implementation and architecture of Retrieval-Augmented Generation (RAG) systems.