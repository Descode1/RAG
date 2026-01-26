import ollama
EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

VECTOR_DB = []

# Loading dataset into memory
dataset = []
with open("cat-facts.txt", "r", encoding="utf-8") as file:
    dataset = file.readlines()
    print(f"Loaded {len(dataset)} entries")

def add_chunk_to_database(chunk):
    embeddings = ollama.embed(model=EMBEDDING_MODEL, input=chunk)['embeddings'][0]
    VECTOR_DB.append((chunk,embeddings))

for i, chunk in enumerate(dataset):
    add_chunk_to_database(chunk)
    print(f"Added chunk {i+1}/{len(dataset)} to the database")