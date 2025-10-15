from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    session_id: str = Field(..., examples=["abc-123"])
    message: str = Field(..., examples=["Wie setze ich mein Passwort zurück?"])

class ChatResponse(BaseModel):
    session_id: str
    answer: str