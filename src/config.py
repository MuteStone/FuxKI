from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    env: str = os.getenv("ENV", "dev")
    llm_provider: str = os.getenv("LLM_PROVIDER", "openai")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")

settings = Settings()