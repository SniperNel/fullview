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
import uuid
from ellar.di import injectable, singleton_scope

class DBItem:
    pk: str

    def __init__(self, **data: t.Dict) -> None:
        self.__dict__ = data

    def __eq__(self, other):
        if isinstance(other, DBItem):
            return self.pk == other.pk
        return self.pk == str(other)

@injectable(scope=singleton_scope)
class RoutineDB:
    def __init__(self) -> None:
        self._data: t.List[DBItem] = []

    def add_routine(self, data: t.Dict) -> str:
        pk = uuid.uuid4()
        _data = dict(data)
        _data.update(pk=str(pk))
        item = DBItem(**_data)
        self._data.append(item)
        return item.pk

    def list(self) -> t.List[DBItem]:
        return self._data

    def update(self, routine_id: str, data: t.Dict) -> t.Optional[DBItem]:
        if routine_id in self._data:
            idx = self._data.index(routine_id)
            _data = dict(data)
            _data.update(pk=str(routine_id))
            self._data[idx] = DBItem(**_data)
            return self._data[idx]

    def get(self, routine_id: str) -> t.Optional[DBItem]:
        if routine_id in self._data:
            idx = self._data.index(routine_id)
            return self._data[idx]

    def remove(self, routine_id: str) -> t.Optional[DBItem]:
        if routine_id in self._data:
            idx = self._data.index(routine_id)
            return self._data.pop(idx)