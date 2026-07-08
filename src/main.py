from read_excel import read_excel
from chunk_documents import chunk_documents
from embeddings import generate_embeddings
from vector_store import build_vector_store
from retriever import retrieve_chunks
from llm import generate_response

documents = read_excel("data/sample_schema_for_rag.xlsx")

chunks = chunk_documents(documents)

embeddings = generate_embeddings(chunks)

vector_store = build_vector_store(embeddings)

print("RAG is ready!")

while True:

    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    retrieved_chunks = retrieve_chunks(
        query=query,
        index=vector_store,
        chunks=chunks,
        k=1
    )

    answer = generate_response(query, retrieved_chunks)

    print("\nAnswer:")
    print(answer)