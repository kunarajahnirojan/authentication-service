from fastapi import FastAPI
from app.api.v1.auth import router as auth_router

app = FastAPI()

# Include routes
app.include_router(auth_router, prefix="api/v1/auth", tags=["Authentication"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Authentication Service"}
