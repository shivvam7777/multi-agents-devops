from fastapi import APIRouter

router = APIRouter()

@router.post("/users")
def create_user():
    return {"status": "created"}

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}

@router.put("/users/{user_id}")
def update_user(user_id: int):
    return {"status": "updated"}

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"status": "deleted"}
