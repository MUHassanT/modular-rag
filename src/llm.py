from ollama import chat

def generate_response(query, retrieved_chunks):

    context = "\n\n".join(
        chunk.page_content for chunk in retrieved_chunks
    )

    response = chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "system",
            "content": """
You are an expert assistant for explaining customer database schemas.

Rules:
- Only use the provided context.
- Never invent information.
- Never answer from your own knowledge.
- If the context does not contain the answer, explicitly say so.
- Mention the exact COLUMN_NAME when answering.
- Include the data type and description whenever available.
- If multiple relevant fields exist, explain each one.
- Keep answers accurate, concise, and professional.
"""
        },
        {
            "role": "user",
            "content": f"""
Database Schema Context:

{context}

Question:

{query}
"""
        }
    ]
)

    return response["message"]["content"]