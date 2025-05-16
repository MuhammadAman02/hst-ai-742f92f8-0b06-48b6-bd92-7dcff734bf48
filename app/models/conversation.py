from pydantic import BaseModel
from typing import List
from datetime import datetime

class Message(BaseModel):
    content: str
    role: str
    timestamp: datetime = datetime.now()

class Conversation(BaseModel):
    id: str
    messages: List[Message] = []