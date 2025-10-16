import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    env: str = os.getenv("ENV", "dev")

    llm_provider: str = os.getenv("LLM_PROVIDER", "openai")

    # OpenAI
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-5-2025-08-07")

    # Ollama
    # ollama_host: str = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
    # ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3")

settings = Settings()