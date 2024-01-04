from langchain.memory import ConversationBufferMemory
from langchain.memory import StreamlitChatMessageHistory

history = StreamlitChatMessageHistory(key="chat_messages")
conversational_memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True, chat_memory=history
)
