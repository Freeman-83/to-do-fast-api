from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    tasks = relationship('Task', back_populates='owner')
