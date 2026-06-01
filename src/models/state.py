from typing import TypedDict
from pydantic import BaseModel

class Queries(BaseModel):
    queries: list[str]


class AgentState(TypedDict):
    task: str
    plan: str
    draft: str
    critique: str
    content: list[str]
    revision_number: int
    max_revisions: int