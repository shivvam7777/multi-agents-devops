from typing import Callable, Dict
from orchestrator.messages import AgentMessage

class Router:
    def __init__(self):
        self.handlers: Dict[str, Callable[[AgentMessage], AgentMessage]] = {}

    def register(self, agent_name: str, handler: Callable[[AgentMessage], AgentMessage]):
        self.handlers[agent_name] = handler

    def send(self, msg: AgentMessage) -> AgentMessage:
        handler = self.handlers.get(msg.receiver)
        if not handler:
            raise ValueError(f"No handler for {msg.receiver}")
        return handler(msg)
