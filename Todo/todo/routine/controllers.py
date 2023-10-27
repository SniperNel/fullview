"""
Define endpoints routes in python class-based fashion
example:

@Controller("/dogs", tag="Dogs", description="Dogs Resources")
class MyController(ControllerBase):
    @get('/')
    def index(self):
        return {'detail': "Welcome Dog's Resources"}
"""
import typing as t
from ellar.common import Controller, ControllerBase, get, delete, put, post
from ellar.common.exceptions import NotFound
from .schemas import RoutineSerializer
from .services import RoutineDB

from ..db.database import engine
from ..db.database import Base

Base.metadata.create_all(bind=engine)

@Controller
class RoutineController(ControllerBase):
    def __init__(self, db: RoutineDB) -> None:
        self.routine_db = db

    @post("/create", response={200: RoutineSerializer})
    async def create_routine(self, routine_data: RoutineSerializer) -> t.Dict:
        routine = self.routine_db.add_routine(routine_data)
        return routine

    @put("/{user_id:str}", response={200: RoutineSerializer})
    async def update_routine(self, user_id: str, routine_id: str, routine_data: RoutineSerializer) -> t.Dict:
        routine = self.routine_db.update(user_id, routine_id, routine_data.dict())
        if not routine:
            raise NotFound("User not Found.")
        return routine

    @delete("/user_routine_id", response={204: dict})
    async def delete_routine(self, user_id: str, routine_id: str) -> t.Optional[int]:
        routine = self.routine_db.remove(user_id, routine_id)
        if not routine:
            raise NotFound("User's routine not found.")
        return 204

    @get("/all", response={200: t.List[RoutineSerializer]})
    async def list(self, user_id: int) -> t.Dict:
        return self.routine_db.list(user_id)

    @get("/status", response={200: t.List[RoutineSerializer]})
    async def list_status(self, user_id: int, status_completed: bool) -> t.Dict:
        return self.routine_db.list_completed(user_id, status_completed)