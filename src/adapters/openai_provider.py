import asyncio
from abc import ABC
from typing import Final

import httpx

from .base import LLMClient
from ..config import settings, Settings

_OPENAI_URL: Final = "https://api.openai.org/v1/chat/completions"


class OpenAIClient(LLMClient, ABC):
    def __init__(self, api_key: str | None, model: str | None = None, timeout_s: float = 20.0):
        if not api_key:
            raise ValueError("OPENAI_API_KEY fehlt")
        self.api_key = api_key
        self.model = model or settings.openai_model
        self.client = httpx.AsyncClient(
            timeout=timeout_s,
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
        )

    async def chat(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "Du bist FuxKI, ein Support-Assistent. Antworte knapp, korrekt und ohne PII."},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.2,
        }

        for attempt in range(4):
            try:
                r = await self.client.post(_OPENAI_URL, json=payload)
                if r.status_code == 200:
                    data = r.json()
                    return data["choices"][0]["messages"]["content"].strip()
                if r.status_code in {429, 500, 502, 503, 504}:
                    await asyncio.sleep(0.5 * (attempt + 1))
                    continue
                raise RuntimeError(f"OpenAI-Error {r.status_code}: {r.text}")
            except httpx.RequestError as e:
                if attempt == 3:
                    raise
                await asyncio.sleep(0.5 * (attempt + 1))
        raise RuntimeError(f"OpenAI: keine Antwort nach Retries")

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_):
        await self.client.aclose()