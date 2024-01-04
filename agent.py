from langchain.agents import Tool, initialize_agent, AgentType
from langchain_core.messages import SystemMessage
from langchain_core.prompts import MessagesPlaceholder

from chatbot.chat_history import conversational_memory
from llm import get_model


def get_super_agent():
    tools = [
        # Tool(
        #     name="",
        #     func=,
        #     description="",
        # ),
    ]

    llm = get_model()
    system_message = SystemMessage(
        content="""
        I want you to act as a customer support agent and help a user with understanding <DOMAIN> support.
        you should answer the question with given tools only and do not use your existing knowledge on the topic.
        If you do not know the answer to a question, you can say "I do not know" and ask user to create a ticket.
        """
    )

    agent_kwargs = {
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
        "system_message": system_message,
    }

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        max_iteration=3,
        memory=conversational_memory,
        handle_parsing_errors=True,
        verbose=True,
        agent_kwargs=agent_kwargs,
    )

    return agent
