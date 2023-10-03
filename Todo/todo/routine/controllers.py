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
from ellar.common import Controller, ControllerBase, get, delete, put, post, Body
from ellar.common.exceptions import NotFound
from .schemas import RoutineSerializer, RetrieveRoutineSerializer
from .services import RoutineDB


@Controller
class RoutineController(ControllerBase):
    def __init__(self, db: RoutineDB) -> None:
        self.routine_db = db

    @get("/{routine_id:str}", response={200: RetrieveRoutineSerializer})
    async def get_routine_by_id(self, routine_id: str):
        routine = self.routine_db.get(routine_id)
        if not routine:
            raise NotFound('Item not found.')
        return routine

    @post("/create", response={200: str})
    async def create_routine(self, payload: RoutineSerializer=Body()):
        pk = self.routine_db.add_routine(payload.dict())
        return pk

    @put("/{routine_id:str}", response={200: RetrieveRoutineSerializer})
    async def update_routine(self, routine_id: str, payload: RoutineSerializer):
        routine = self.routine_db.update(routine_id, payload.dict())
        if not routine:
            raise NotFound("Item not Found.")
        return routine

    @delete("/{routine_id:str}", response={204: dict})
    async def delete_routine(self, routine_id: str):
        routine = self.routine_db.remove(routine_id)
        if not routine:
            raise NotFound("Item not found.")
        return 204, {}

    @get("/", response={200: t.List[RetrieveRoutineSerializer]})
    async def list(self):
        return self.routine_db.list()