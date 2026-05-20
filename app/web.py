import os
import streamlit as st
from PIL import Image

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
    page_title="Menlo College AI Agent",
    page_icon="🎓",
    layout="wide"
)

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
        "Powered by NVIDIA LLM API + Canvas + Menlo Knowledge Tools"
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

question = st.text_input(
    "Ask the Menlo AI Agent:",
    placeholder="Example: What assignments are due this week?"
)

# =====================================
# Ask Agent Button
# =====================================

if st.button("Ask Agent"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            context = route_and_collect_context(question)

            answer = ask_nemotron(question, context)

        st.subheader("Answer")

        st.success(answer)

        with st.expander("Retrieved Context"):

            st.text(context)

