import os
from PIL import Image
import streamlit as st
from router import route_and_collect_context
from llm import ask_nemotron



# =====================================
# Load Streamlit Secrets or Local .env
# =====================================

try:
    for key, value in st.secrets.items():
        os.environ[key] = str(value)
except Exception:
    from dotenv import load_dotenv
    load_dotenv()

# =====================================
# Local Imports
# =====================================

from router import route_and_collect_context
from llm import ask_nemotron

# =====================================
# Streamlit Page Config
# =====================================

st.set_page_config(
    page_title="Menlo College Canvas AI Agent",
    page_icon="🎓",
    layout="wide"
)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617 0%, #0f172a 45%, #1e1b4b 100%);
    color: white;
}

.block-container {
    max-width: 1200px;
    padding-top: 1rem;
    padding-bottom: 6rem;
}

h1, h2, h3, p {
    color: white;
}

[data-testid="stSidebar"] {
    background: #020617;
}

[data-testid="stChatMessageContent"] {
    background: rgba(15, 23, 42, 0.95);
    border: 1px solid rgba(99,102,241,.35);
    border-radius: 20px;
    padding: 16px 20px;
}

div[data-testid="stChatInput"] {
    background: #0f172a;
    border: 2px solid #6366f1;
    border-radius: 18px;
}
</style>
""", unsafe_allow_html=True)









# =====================================
# Header with Menlo Logo
# =====================================

logo = Image.open("assets/Menlo_College_logo.svg.png")

col1, col2 = st.columns([1, 5])

with col1:
    st.image(logo, width=160)

with col2:
    st.title("Menlo College AI Agent")
    st.caption(
        "Powered by NVIDIA LLM API + Canvas"
    )

# =====================================
# Sidebar Agent Tools
# =====================================

with st.sidebar:

    st.header("Agent Tools")

    st.checkbox(
        "Canvas Assignments",
        value=os.getenv(
            "ENABLE_CANVAS_ASSIGNMENTS",
            "true"
        ).lower() == "true",
        disabled=True
    )

    st.checkbox(
        "Canvas Announcements",
        value=os.getenv(
            "ENABLE_CANVAS_ANNOUNCEMENTS",
            "true"
        ).lower() == "true",
        disabled=True
    )

    st.checkbox(
        "Menlo Website Q&A",
        value=os.getenv(
            "ENABLE_WEBSITE_QA",
            "true"
        ).lower() == "true",
        disabled=True
    )

    st.checkbox(
        "Email Drafting",
        value=os.getenv(
            "ENABLE_EMAIL_AGENT",
            "false"
        ).lower() == "true",
        disabled=True
    )

    st.checkbox(
        "IT Helpdesk",
        value=os.getenv(
            "ENABLE_IT_AGENT",
            "false"
        ).lower() == "true",
        disabled=True
    )

    st.checkbox(
        "Advising Agent",
        value=os.getenv(
            "ENABLE_ADVISING_AGENT",
            "false"
        ).lower() == "true",
        disabled=True
    )

# =====================================
# Main Chat Input
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask Menlo AI...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            context = route_and_collect_context(question)
            answer = ask_nemotron(question, context)
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})


# =====================================
# Footer
# =====================================

st.markdown("---")

st.caption(
    "© 2026 Menlo College AI Agent • All rights reserved • Created by Dr. Sarina Adeli"
)

