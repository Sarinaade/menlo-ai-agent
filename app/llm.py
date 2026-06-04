from openai import OpenAI
from config import settings

SYSTEM_PROMPT = """You are Menlo AI Campus Agent MVP.
You answer only from provided tool context.
If the context is insufficient, say what is missing.
Do not reveal private student data.
For Canvas data, summarize assignments and announcements clearly.
For website data, cite page titles or URLs when available."""

def ask_nemotron(user_question: str, context: str) -> str:
    if not settings.nvidia_api_key:
        return (
            "NVIDIA_API_KEY is not set. Tool context retrieved successfully, "
            "but the LLM response was skipped.\n\n"
            f"Retrieved context:\n{context[:2000]}"
        )

    client = OpenAI(
        api_key=settings.nvidia_api_key,
        base_url=settings.nvidia_base_url,
    )

    response = client.chat.completions.create(
	model="meta/llama-3.1-8b-instruct",
        temperature=0.2,
        max_tokens=900,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Question:\n{user_question}\n\nTool context:\n{context}"},
        ],
    )
    return response.choices[0].message.content
