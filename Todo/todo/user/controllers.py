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
from ellar.common import Controller, ControllerBase, get, post
from ellar.common.exceptions import NotFound
from .schemas import UserSerializer
from .services import UserService




@Controller("/user")
class UserController(ControllerBase):
    def __init__(self, userDB: UserService) -> None:
        self.db = userDB

    @post("/add", response={200: UserSerializer})
    async def create_user(self, user_data: UserSerializer) -> t.Dict:
        user = self.db.create_user(user_data)
        return user

    @get("/", response={200: t.List[UserSerializer]})
    async def list_all_users(self) -> t.Dict:
        return self.db.get_all_users()

    @get("/{user_id:str}", response={200: UserSerializer})
    async def get_user_by_id(self, user_id: int) -> t.Optional[dict]:
        user = self.db.get_user_by_id(user_id)
        if not user:
            raise NotFound("User not found")
        return user