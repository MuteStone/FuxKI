# FuxKI (PoC)
FastAPI-basierter Prototyp für First/Second-Level-Support + Chatbot.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
cp .env.example .env  # OPENAI_API_KEY setzen
pre-commit install
uvicorn src.api.main:app --reload
