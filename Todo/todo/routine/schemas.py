"""
Define Serializers/DTOs
Example:

class ASampleDTO(Serializer):
    name: str
    age: t.Optional[int] = None

for dataclasses, Inherit from DataclassSerializer

@dataclass
class ASampleDTO(DataclassSerializer):
    name: str
    age: t.Optional[int] = None
"""

from ellar.common import Serializer



class RoutineSerializer(Serializer):
    morning: str
    afternoon: str
    night: str
    status_completed: bool
    user_id: int

class RetrieveRoutineSerializer(RoutineSerializer):
    pk: str