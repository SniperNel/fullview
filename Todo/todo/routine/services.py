"""
Create a provider and declare its scope

@injectable
class AProvider
    pass

@injectable(scope=transient_scope)
class BProvider
    pass
"""
import typing as t
from ellar.di import injectable, singleton_scope


from ..db.database import get_session_maker
from ..db.models import Routine


@injectable(scope=singleton_scope)
class RoutineDB:
    def __init__(self) -> None:
        self.db = get_session_maker()


    def add_routine(self, routine_data) -> t.Dict:
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

    def list(self, user_id) -> t.Dict:
        routines = self.db.query(Routine).filter(Routine.user_id == user_id).all()
        return routines

    def list_completed(self, user_id, status_completed) -> t.Dict:
        routines = self.db.query(Routine).filter(Routine.user_id == user_id, Routine.status_completed == status_completed).all()
        return routines


    def update(self, routine_id, user_id, update_data) -> t.Dict:
        routine = self.db.query(Routine).filter(Routine.id == routine_id, Routine.user_id == user_id)
        routine.update(update_data)
        self.db.commit()
        return routine


    def remove(self, routine_id, user_id) -> None:
        delete = self.db.query(Routine).filter(Routine.id == routine_id, Routine.user_id == user_id).delete()
        self.db.commit()
        return delete
