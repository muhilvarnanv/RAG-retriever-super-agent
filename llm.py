from langchain.chat_models import ChatVertexAI


def get_model():
    return ChatVertexAI(temperature=0.9)
