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
from dataclasses import dataclass

from ellar.common import Serializer, DataclassSerializer
from pydantic.networks import EmailStr

@dataclass
class UserCredentials(DataclassSerializer):
    email: EmailStr
    password: str

class RoutineSerializer(Serializer):
    morning: str
    afternoon: str
    night: str

class RetrieveRoutineSerializer(RoutineSerializer):
    pk: str