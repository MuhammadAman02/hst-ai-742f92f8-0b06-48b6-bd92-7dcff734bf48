from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.medical_chatbot import MedicalChatbotService
from app.models.conversation import Conversation, Message

router = APIRouter()

chatbot_service = MedicalChatbotService()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    conversation: Conversation

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    conversation = chatbot_service.create_conversation()
    chatbot_service.add_message(conversation, request.message, "user")
    
    response = chatbot_service.get_response(request.message)
    chatbot_service.add_message(conversation, response, "assistant")
    
    return ChatResponse(response=response, conversation=conversation)

@router.get("/conversation/{conversation_id}", response_model=Conversation)
async def get_conversation(conversation_id: str):
    # In a real application, you would retrieve the conversation from a database
    # For this example, we'll just return a new conversation
    return chatbot_service.create_conversation()