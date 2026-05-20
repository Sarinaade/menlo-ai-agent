from canvas_tool import canvas_context
from website_tool import search_menlo_website

def route_and_collect_context(question: str) -> str:
    q = question.lower()

    canvas_keywords = [
        "assignment", "assignments", "due", "deadline",
        "announcement", "canvas", "course", "homework"
    ]

    website_keywords = [
        "menlo", "policy", "program", "admission", "academics",
        "tuition", "faculty", "student life", "calendar"
    ]

    contexts = []

    if any(k in q for k in canvas_keywords):
        contexts.append(canvas_context())

    if any(k in q for k in website_keywords) or not contexts:
        contexts.append(search_menlo_website(question))

    return "\n\n---\n\n".join(contexts)
