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
from ellar.core import Config

from ..db.database import get_session_maker
from ..db.models import Routine


@injectable(scope=singleton_scope)
class RoutineDB:
    def __init__(self, config: Config) -> None:
        session_maker = get_session_maker(config)
        self.db = session_maker()


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


    def update(self, user_id, routine_id, update_data) -> t.Dict:
        routine = self.db.query(Routine).filter(Routine.user_id == user_id, Routine.id == routine_id)
        routine.update(update_data)
        self.db.commit()
        return routine.first()


    def remove(self, user_id, routine_id) -> None:
        delete = self.db.query(Routine).filter(Routine.user_id == user_id, Routine.id == routine_id).delete()
        self.db.commit()
        return delete
