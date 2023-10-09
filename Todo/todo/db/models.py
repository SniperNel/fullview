from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from todo.db.database import Base


class Routine(Base):
    __tablename__ = "routines"

    id = Column(Integer, primary_key=True, index=True)
    morning = Column(String, index=True)
    afternoon = Column(String, index=True)
    night = Column(String, index=True)
