from fastapi import FastAPI
from orchestrator.router import Router
from orchestrator.messages import AgentMessage, Task
from agents import planner

app = FastAPI()
router = Router()

# register planner agent
router.register("planner", planner.handle)

@app.post("/run")
def run(task: Task):
    msg = AgentMessage(
        sender="user",
        receiver="planner",
        type="PLAN",
        payload=task.model_dump(),
    )
    response = router.send(msg)
    return {"result": response.payload}
