from langchain_core.messages import SystemMessage, HumanMessage
from src.config import model
from src.prompts.templates import WRITER_PROMPT
from src.models.state import AgentState

def generation_node(state: AgentState):
    content = "\n\n".join(state['content'] or [])
    user_message = HumanMessage(
        content=f"{state['task']}\n\nHere is my plan:\n\n{state['plan']}"
    )
    messages = [
        SystemMessage(
            content=WRITER_PROMPT.format(content=content)
        ),
        user_message
    ]
    response = model