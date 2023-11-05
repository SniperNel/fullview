from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from todo.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    first_name = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    routines = relationship('Routine', back_populates='users')


class Routine(Base):
    __tablename__ = "routines"

    id = Column(Integer, primary_key=True, index=True)
    morning = Column(String, index=True)
    afternoon = Column(String, index=True)
    night = Column(String, index=True)
    status_completed = Column("completed", Boolean, default=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    users = relationship('User', back_populates='routines')