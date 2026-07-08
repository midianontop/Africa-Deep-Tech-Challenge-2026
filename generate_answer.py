import ollama

def generate_answer(question, context):

    prompt = f"""
You are an African cybersecurity assistant.

Answer the user's question clearly and professionally.

Use the provided context as your source of information.

Do not mention the context.
Do not mention that you are an AI assistant.
Do not say "Based on the context provided".
Do not invent facts.

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]