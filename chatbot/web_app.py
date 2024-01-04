import time
import streamlit as st
from streamlit_chat import message

from agent import get_super_agent
from chatbot.chat_history import history


def render_chat_history():
    for history_message in history.messages:
        message(
            history_message.content,
            is_user=history_message.type != "ai",
            key=str(time.time()),
        )


def load_web_app():
    st.title("AI Support Agent")

    query = st.text_input("Enter Your Request: ")

    if query:
        agent = get_super_agent()
        agent.invoke(query)
        render_chat_history()
