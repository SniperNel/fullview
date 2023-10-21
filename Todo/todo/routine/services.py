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

from ..db.models import Routine, User
from ..db.database import SessionLocal


@injectable(scope=singleton_scope)
class RoutineDB:
    def __init__(self) -> None:
        self.db = SessionLocal()

    def add_routine(self, routine_data):
        routine = Routine(morning=routine_data.morning,
                          afternoon=routine_data.afternoon,
                          night=routine_data.night,
                          status_completed=routine_data.status_completed,
                          user_id=routine_data.user_id,
                          )
        self.db.add(routine)
        self.db.commit()
        self.db.refresh(routine)
        return routine

    def list(self, user_id):
        routines = self.db.query(Routine).filter(Routine.user_id == user_id).all()
        return routines

    def list_completed(self, user_id, status_completed):
        routines = self.db.query(Routine).filter(Routine.user_id == user_id, Routine.status_completed == status_completed).all()
        return routines


    def update(self, user_id, routine_id, update_data):
        routine = self.db.query(Routine).filter(Routine.user_id == user_id, Routine.id == routine_id)
        routine.update(update_data)
        self.db.commit()
        return routine.first()


    def remove(self, user_id, routine_id):
        delete = self.db.query(Routine).filter(Routine.user_id == user_id, Routine.id == routine_id).delete()
        self.db.commit()
        return delete
