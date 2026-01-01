from pydantic import BaseModel
from typing import List, Optional

class Task(BaseModel):
    id: str
    title: str
    description: str
    acceptance_criteria: List[str]

class CodeArtifact(BaseModel):
    path: str
    language: str
    content: str

class TestResult(BaseModel):
    passed: bool
    details: str
    coverage: Optional[float] = None

class AgentMessage(BaseModel):
    sender: str
    receiver: str
    type: str  # "PLAN", "CODE", "TEST", "DEPLOY", "DONE"
    payload: dict
