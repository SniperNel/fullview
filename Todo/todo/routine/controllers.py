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
from .schemas import RoutineSerializer, RetrieveRoutineSerializer
from .services import RoutineDB

from ..db.database import engine
from ..db.database import Base

Base.metadata.create_all(bind=engine)

@Controller
class RoutineController(ControllerBase):
    def __init__(self, db: RoutineDB) -> None:
        self.routine_db = db

    @get("/{routine_id:str}", response={200: RoutineSerializer})
    async def get_routine_by_id(self, routine_id: int):
        routine = self.routine_db.get(routine_id)
        if not routine:
            raise NotFound('Item not found.')
        return routine

    @post("/create", response={200: RoutineSerializer})
    async def create_routine(self, routine_data: RoutineSerializer):
        routine = self.routine_db.add_routine(routine_data)
        return routine

    @put("/{routine_id:str}", response={200: RoutineSerializer})
    async def update_routine(self, routine_id: int, routine_data: RoutineSerializer):
        routine = self.routine_db.update(routine_id, routine_data)
        if not routine:
            raise NotFound("Item not Found.")
        return routine

    @delete("/{routine_id:str}", response={204: dict})
    async def delete_routine(self, routine_id: int):
        routine = self.routine_db.remove(routine_id)
        if not routine:
            raise NotFound("Item not found.")
        return 204, {}

    @get("/", response={200: t.List[RoutineSerializer]})
    async def list(self):
        return self.routine_db.list()