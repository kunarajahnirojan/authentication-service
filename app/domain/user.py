from sqlalchemy import Column, Integer, String, Boolean
from app.infrastructure.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150), unique=True, index=True, nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    password = Column(String(200), nullable=False)
    is_active = Column(Boolean, default=True)
