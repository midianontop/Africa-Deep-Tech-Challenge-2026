from retriever import search_documents
from generate_answer import generate_answer


while True:

    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        break

    results = search_documents(question)

    context = "\n\n".join(results)

    answer = generate_answer(
        question,
        context
    )

    print("\nANSWER:")
    print("=" * 60)
    print(answer)