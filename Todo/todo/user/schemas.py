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

import typing
from datetime import datetime
from pydantic import Field

from ellar.common import Serializer


class UserSerializer(Serializer):
    id: typing.Optional[int]
    email: str
    first_name: str
    last_name: str
    is_active:bool
    created_date: datetime = Field(default_factory=datetime.now)

class RetrieveUserSerializer(UserSerializer):
    pk: str