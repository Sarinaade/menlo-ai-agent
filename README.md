# Menlo NVIDIA Agent MVP

Read-only MVP:
1. Menlo website Q&A
2. Canvas assignment / announcement assistant
3. NVIDIA-hosted Nemotron-compatible chat completion via NVIDIA API Catalog
4. Safe mock Canvas mode by default

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# add your NVIDIA_API_KEY
python app/ingest_website.py
python app/main.py "What assignments are due this week?"
python app/main.py "What does Menlo say about AI or academics?"
```

## Environment

`NVIDIA_API_KEY` is required for real LLM responses.  
`CANVAS_API_TOKEN` is optional. If omitted, the app uses `data/canvas_mock.json`.

## Production note

Keep the first pilot read-only. Do not allow the agent to send emails, change grades, update Canvas, or modify IT systems until RBAC, audit logging, and human approval are implemented.
