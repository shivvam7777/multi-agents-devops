from orchestrator.router import Router
from orchestrator.messages import AgentMessage, Task, CodeArtifact, TestResult
import os

# Planner Agent
def planner_handler(msg: AgentMessage) -> AgentMessage:
    task = Task(
        id="T-001",
        title="User Management API",
        description="User CRUD endpoints",
        acceptance_criteria=["Create", "Read", "Update", "Delete"]
    )
    return AgentMessage(sender="planner", receiver=msg.sender, type="PLAN", payload=task.model_dump())

# Coder Agent
def coder_handler(msg: AgentMessage) -> AgentMessage:
    artifact = CodeArtifact(
        path="services/user_api.py",
        language="python",
        content="""from fastapi import APIRouter

router = APIRouter()

@router.post('/users')
def create_user():
    return {'status': 'created'}

@router.get('/users/{user_id}')
def get_user(user_id: int):
    return {'id': user_id}

@router.put('/users/{user_id}')
def update_user(user_id: int):
    return {'status': 'updated'}

@router.delete('/users/{user_id}')
def delete_user(user_id: int):
    return {'status': 'deleted'}
"""
    )
    return AgentMessage(sender="coder", receiver=msg.sender, type="CODE", payload=artifact.model_dump())

# Tester Agent
def tester_handler(msg: AgentMessage) -> AgentMessage:
    result = TestResult(passed=True, details="All tests passed", coverage=90.0)
    return AgentMessage(sender="tester", receiver=msg.sender, type="TEST", payload=result.model_dump())

# CI/CD Agent
def cicd_handler(msg: AgentMessage) -> AgentMessage:
    status = "Deployment successful" if msg.payload.get("passed") else "Deployment failed"
    return AgentMessage(sender="cicd", receiver=msg.sender, type="DEPLOY", payload={"status": status})

# Router setup
router = Router()
router.register("planner", planner_handler)
router.register("coder", coder_handler)
router.register("tester", tester_handler)
router.register("cicd", cicd_handler)

if __name__ == "__main__":
    plan = router.send(AgentMessage(sender="client", receiver="planner", type="PLAN", payload={}))
    print("Plan:", plan.payload)

    code = router.send(AgentMessage(sender="client", receiver="coder", type="CODE", payload=plan.payload))
    print("Code:", code.payload)

    # 👉 नया स्टेप: CodeArtifact को फ़ाइल में लिखना
    os.makedirs(os.path.dirname(code.payload["path"]), exist_ok=True)
    with open(code.payload["path"], "w") as f:
        f.write(code.payload["content"])
    print(f"Code written to {code.payload['path']}")

    test = router.send(AgentMessage(sender="client", receiver="tester", type="TEST", payload=code.payload))
    print("Test:", test.payload)

    deploy = router.send(AgentMessage(sender="client", receiver="cicd", type="DEPLOY", payload=test.payload))
    print("Deploy:", deploy.payload)
