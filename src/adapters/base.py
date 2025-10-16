from abc import ABC, abstractmethod


class LLMClient(ABC):
    @abstractmethod
    async def connect(self, prompt: str) -> str: ...