import sys
from dotenv import load_dotenv

load_dotenv()

from app.router import route_and_collect_context
from app.llm import ask_nemotron

def main():
    question = " ".join(sys.argv[1:]).strip()
    if not question:
        question = input("Ask Menlo Agent: ")

    context = route_and_collect_context(question)
    answer = ask_nemotron(question, context)

    print("\n=== Menlo Agent Answer ===\n")
    print(answer)

if __name__ == "__main__":
    main()
