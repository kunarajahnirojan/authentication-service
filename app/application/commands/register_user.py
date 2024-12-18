from sqlalchemy.orm import Session
from app.domain.user import User
from app.infrastructure.database import SessionLocal

def register_user(user_data: dict):
    db: Session = SessionLocal()
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
