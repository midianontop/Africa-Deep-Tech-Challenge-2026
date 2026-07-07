import ollama

def generate_answer(question, context):

    prompt = f"""
You are an offline African cybersecurity assistant.

Use the provided context to answer the question.

Provide a detailed answer.

If the context contains information about a person,
include their education, training, interests, and goals.

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