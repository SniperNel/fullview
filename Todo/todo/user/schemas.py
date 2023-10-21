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