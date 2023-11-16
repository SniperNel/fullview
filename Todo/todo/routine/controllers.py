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
from typing import Optional
from ellar.common import Controller, ControllerBase, get, delete, post, put
from ellar.common.exceptions import NotFound
from .schemas import RoutineSerializer, RetrieveRoutineSerializer
from .services import RoutineDB


@Controller
class RoutineController(ControllerBase):
    def __init__(self, routinedb: RoutineDB) -> None:
        self.db = routinedb

    @post("/create", response={200: RoutineSerializer})
    async def create_routine(self, routine_data: RoutineSerializer) -> t.Dict:
        routine = self.db.add_routine(routine_data)
        return routine

    @put("/{user_id}/{routine_id}", response={200: RoutineSerializer})
    async def update_routine(self, routine_id: int, user_id: int, routine_data: RoutineSerializer) -> Optional[RoutineSerializer]:
        update_data = routine_data.dict(exclude_unset=True)
        routine = self.db.update(routine_id, user_id, update_data)
        if not routine:
            raise NotFound("User not Found.")
        return RoutineSerializer.from_orm(routine)

    @delete("/{user_id}/{routine_id}", response={200: dict})
    async def delete_routine(self, user_id: int, routine_id: int) -> t.Optional[int]:
        routine = self.db.remove(user_id, routine_id)
        if not routine:
            raise NotFound("User's routine not found.")
        return 200, {}

    @get("/all/{user_id:str}", response={200: t.List[RoutineSerializer]})
    async def list(self, user_id: int) -> t.Dict:
        return self.db.list(user_id)

    @get("/status/{user_id:str}", response={200: t.List[RoutineSerializer]})
    async def list_status(self, user_id: int, status_completed: bool) -> t.Dict:
        return self.db.list_completed(user_id, status_completed)