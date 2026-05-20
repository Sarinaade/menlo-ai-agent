import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="Menlo College AI Agent",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Menlo College AI Agent")
st.caption("Powered by NVIDIA LLM API + Canvas + Menlo Knowledge Tools")

with st.sidebar:
    st.header("Agent Tools")
    st.write("✅ Canvas Assignments")
    st.write("✅ Canvas Announcements")
    st.write("✅ Menlo Website Q&A")
    st.write("⬜ Email Drafting")
    st.write("⬜ IT Helpdesk")
    st.write("⬜ Advising Agent")

question = st.text_input(
    "Ask the Menlo AI Agent:",
    placeholder="Example: What assignments are due this week?"
)

if st.button("Ask Agent"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = requests.post(API_URL, json={"question": question})

        if response.status_code == 200:
            data = response.json()

            st.subheader("Answer")
            st.success(data["answer"])

            with st.expander("Retrieved Context"):
                st.text(data["context"])
        else:
            st.error("API error. Make sure FastAPI is running.")
            st.text(response.text)

