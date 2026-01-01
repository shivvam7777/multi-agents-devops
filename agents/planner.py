from orchestrator.messages import AgentMessage

def simple_decompose(spec: dict):
    title = spec.get("title", "App")
    return [
        {"id": "t1", "title": f"Design {title} API", "desc": "Define endpoints & models"},
        {"id": "t2", "title": "Implement core logic", "desc": "Service layer functions"},
        {"id": "t3", "title": "Write unit tests", "desc": "PyTest for services"},
        {"id": "t4", "title": "Package & deploy", "desc": "Dockerize & stub deploy"},
    ]

def handle(msg: AgentMessage) -> AgentMessage:
    spec = msg.payload
    plan = {"tasks": simple_decompose(spec)}
    return AgentMessage(
        sender="planner",
        receiver="coder",
        type="CODE",
        payload=plan,
    )
