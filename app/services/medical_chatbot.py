import random
from app.models.conversation import Message, Conversation

class MedicalChatbotService:
    def __init__(self):
        self.responses = {
            "greeting": [
                "Hello! I'm a medical chatbot. How can I assist you today?",
                "Welcome! I'm here to provide basic medical information. How may I help you?"
            ],
            "disclaimer": [
                "Please note that I'm an AI assistant and cannot provide professional medical advice. Always consult with a qualified healthcare provider for medical concerns.",
                "Remember, I'm not a substitute for professional medical advice. Please consult a doctor for any health-related issues."
            ],
            "general": [
                "I can provide general information about common medical conditions and symptoms. What would you like to know?",
                "I can offer basic health tips and information. What topic are you interested in?"
            ],
            "unknown": [
                "I'm sorry, but I don't have enough information to answer that question. Please consult a healthcare professional for specific medical advice.",
                "That's beyond my current capabilities. For accurate information, please speak with a doctor or medical expert."
            ]
        }

    def get_response(self, user_message: str) -> str:
        lower_message = user_message.lower()
        
        if any(word in lower_message for word in ["hello", "hi", "hey"]):
            return random.choice(self.responses["greeting"])
        elif "disclaimer" in lower_message:
            return random.choice(self.responses["disclaimer"])
        elif any(word in lower_message for word in ["symptom", "condition", "disease", "treatment"]):
            return random.choice(self.responses["general"]) + "\n\n" + random.choice(self.responses["disclaimer"])
        else:
            return random.choice(self.responses["unknown"])

    def create_conversation(self) -> Conversation:
        return Conversation(id=str(random.randint(1000, 9999)))

    def add_message(self, conversation: Conversation, content: str, role: str) -> None:
        conversation.messages.append(Message(content=content, role=role))