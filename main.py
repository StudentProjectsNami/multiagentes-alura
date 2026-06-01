from src.config import *
from src.models.state import AgentState
from src.prompts.templates import *
from langchain_google_genai import ChatGoogleGenerativeAI   

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperatura=0)

