from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_chunks(query, index, chunks, k=1):

    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, k)
    retrieved_chunks = [chunks[i] for i in indices[0]]
    
    return retrieved_chunks