"""
Create a provider and declare its scope

@injectable
class AProvider
    pass

@injectable(scope=transient_scope)
class BProvider
    pass
"""

from ellar.di import injectable, singleton_scope

from ..db.models import Routine
from ..db.database import SessionLocal


@injectable(scope=singleton_scope)
class RoutineDB:
    def __init__(self) -> None:
        self.db = SessionLocal()

    def add_routine(self, routine_data):
        routine = Routine(morning=routine_data.morning, afternoon=routine_data.afternoon, night=routine_data.night)
        self.db.add(routine)
        self.db.commit()
        self.db.refresh(routine)
        return routine

    def list(self):
        routines = self.db.query(Routine).all()
        return routines

    def update(self, routine_id, update_data):
        routine = self.db.query(Routine).filter(Routine.id == routine_id)
        routine.update(update_data)
        self.db.commit()
        return routine.first()

    def get(self, routine_id):
        return self.db.query(Routine).filter(Routine.id == routine_id).first()

    def remove(self, routine_id):
        delete = self.db.query(Routine).filter(Routine.id == routine_id).delete()
        self.db.commit()
        return delete