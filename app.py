import streamlit as st
from retriever import search_documents
from generate_answer import generate_answer
from threat_detector import detect_threat
from incident_response import get_incident_response
from confidence import get_confidence

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
    - Retrieval-Augmented Generation (RAG)
    - ChromaDB Vector Search
    - Llama 3.2 Local LLM
    - Cybersecurity Knowledge Base
    - Threat Detection
    - Incident Response Recommendations
    - Confidence Score
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

# ====================================
# Display Chat History
# ====================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        if msg["role"] == "assistant":

            st.write(f"🛡️ Threat Type: {msg['threat']}")
            st.write(f"⚠️ Severity: {msg['severity']}")
            st.write(f"📊 Confidence: {msg['confidence']}")

            st.write(msg["content"])

            st.write("### Recommended Actions")

            for action in msg["recommendations"]:
                st.write(f"✅ {action}")

        else:
            st.write(msg["content"])

# ====================================
# Chat Input
# ====================================

question = st.chat_input(
    "Ask a cybersecurity question..."
)

# ====================================
# Process Question
# ====================================

if question:

    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    with st.spinner("Analyzing threat and generating answer..."):

        # Threat Detection
        threat_type, severity = detect_threat(question)

        # Confidence Score
        confidence = get_confidence(severity)

        # Incident Response Recommendations
        recommendations = get_incident_response(
            threat_type
        )

        # Retrieve Documents
        results = search_documents(question)

        # Build Context
        context = "\n\n".join(results)

        # Generate AI Answer
        ai_answer = generate_answer(
            question,
            context
        )

    # Save Assistant Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_answer,
            "threat": threat_type,
            "severity": severity,
            "confidence": confidence,
            "recommendations": recommendations
        }
    )

    # Display Assistant Response
    with st.chat_message("assistant"):

        st.write(f"🛡️ Threat Type: {threat_type}")
        st.write(f"⚠️ Severity: {severity}")
        st.write(f"📊 Confidence: {confidence}")

        st.write(ai_answer)

        st.write("### Recommended Actions")

        for action in recommendations:
            st.write(f"✅ {action}")