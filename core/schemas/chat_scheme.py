from pydantic import BaseModel

class SendMessageScheme(BaseModel):
    text: str