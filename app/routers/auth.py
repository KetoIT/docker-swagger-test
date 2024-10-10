from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def register(user: dict):
    return {"message": "You are registered!"}
