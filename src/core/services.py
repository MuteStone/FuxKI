from ..adapters.base import LLMClient
from .schemas import ChatRequest, ChatResponse

# Hier landen später: RAG, Tools (Ticket/AD/Wiki), Policies/Guardrails


async def handle_chat(req: ChatRequest, llm: LLMClient) -> ChatResponse:
    answer = await llm.chat(req.message)
    return ChatResponse(session_id=req.seission_id, answer=answer)
