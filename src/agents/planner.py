from langchain_core.messages import SystemMessage, HumanMessage
from src.config import model
from src.prompts.templates import PLAN_PROMPT
from src.models.state import AgentState

def plan_node(state: AgentState):
    messages = [
        SystemMessage(content=PLAN_PROMPT),
        HumanMessage(content=state['task'])
    ]
    response = model.invoke(messages)
    return {"plan": response.content}