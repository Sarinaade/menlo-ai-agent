from fastapi import FastAPI
from pydantic import BaseModel
from app.router import route_and_collect_context
from app.llm import ask_nemotron

app = FastAPI(title="Menlo AI Agent API")

class AgentRequest(BaseModel):
    question: str

class AgentResponse(BaseModel):
    answer: str
    context: str

@app.get("/")
def home():
    return {"message": "Menlo AI Agent API is running"}

@app.post("/ask", response_model=AgentResponse)
def ask_agent(request: AgentRequest):
    context = route_and_collect_context(request.question)
    answer = ask_nemotron(request.question, context)

    return AgentResponse(
        answer=answer,
        context=context
    )


