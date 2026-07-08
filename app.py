import streamlit as st
from retriever import search_documents
from generate_answer import generate_answer

# ====================================
# Page Configuration
# ====================================

st.set_page_config(
    page_title="African Cybersecurity AI Assistant",
    page_icon="🛡️",
    layout="wide"
)

# ====================================
# Session State
# ====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ====================================
# Sidebar
# ====================================

with st.sidebar:
    st.title("🛡️ About")

    st.write("""
    **African Cybersecurity AI Assistant**

    Built by: Midian

    Features:
    - Offline AI
    - RAG (Retrieval-Augmented Generation)
    - ChromaDB Vector Search
    - Llama 3.2 Local LLM
    - Cybersecurity Knowledge Base
    """)

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ====================================
# Main Page
# ====================================

st.title("🛡️ African Cybersecurity AI Assistant")

st.write(
    "Ask cybersecurity questions and get answers from the local knowledge base."
)

question = st.text_input("Enter your question:")

# ====================================
# Ask Button
# ====================================

if st.button("Ask"):

    if question.strip():

        with st.spinner("Searching and generating answer..."):

            results = search_documents(question)

            context = "\n\n".join(results)

            answer = generate_answer(
                question,
                context
            )

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "sources": results
                }
            )

# ====================================
# Chat History
# ====================================

st.markdown("---")

for msg in st.session_state.messages:

    if msg["role"] == "user":

        st.markdown("### 👤 You")
        st.write(msg["content"])

    else:

        st.markdown("### 🛡️ AI Assistant")
        st.write(msg["content"])

        if "sources" in msg:

            with st.expander("📚 Retrieved Sources"):

                for i, chunk in enumerate(msg["sources"], start=1):
                    st.write(f"Source {i}")
                    st.text(chunk[:500] + "...")

    st.markdown("---")