from .base import LLMClient

class OpenAIClient(LLMClient):
    def __init__(self, api_key: str | None):
        self.api_key = api_key

    async def chat(self, prompt: str) -> str:
        # Todo: echte OpenAI/Azure/Anthropic-Anbindung
        return f"[Stub-LLM] Antwort auf: {prompt[:60]}..."