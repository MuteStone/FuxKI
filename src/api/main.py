from fastapi import Depends, FastAPI, HTTPException

from ..adapters.openai_provider import OpenAIClient
from ..config import settings
from ..core.schemas import ChatRequest, ChatResponse
from ..core.services import handle_chat

app = FastAPI(
    title="FuxKI Support API",
    description="Interne API zur Verarbeitung von Supportanfragen mit LLM-Integration",
    version="0.1.0",
)


def get_llm():
    if settings.llm_provider == "openai" and not settings.openai_api_key:
        raise HTTPException(500, "OPENAI_API_KEY fehlt - .env konfigurieren")
    return OpenAIClient(api_key=settings.openai_api_key)


@app.get("/health")
async def health():
    return {"status": "ok", "env": settings.env}


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest, llm=Depends(get_llm)):
    return await handle_chat(req, llm)
