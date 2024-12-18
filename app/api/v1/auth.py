from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/register")
def register_user(user: dict):
    return {"message": "User registered successfully", "user": user}

@router.post("/login")
def login_user(credentials: dict):
    return {"message": "Login successful", "user": credentials}

@router.get("/me")
def get_profile(user_id: int):
    return {"message": "User profile data", "user_id": user_id}
