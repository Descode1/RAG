# Simple RAG Chatbot with Ollama

This project demonstrates a basic Retrieval-Augmented Generation (RAG) system using Ollama for embeddings and chat responses.

## Features

- Loads text data from a file
- Converts text chunks into vector embeddings
- Stores embeddings in memory
- Retrieves the most relevant chunks using cosine similarity
- Uses retrieved context to answer user queries

## Requirements

- Python 3.9+
- Ollama installed and running
- Models:
  - `hf.co/CompendiumLabs/bge-base-en-v1.5-gguf` (embeddings)
  - `hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF` (chat)

## How It Works

1. Reads data from `cat-facts.txt`
2. Embeds each line and stores it in a vector database
3. When a question is asked:
   - The query is embedded
   - Similarity is calculated against all stored vectors
   - The most relevant chunks are retrieved
4. The chatbot answers using only the retrieved context

## Usage

```bash
python main.py
