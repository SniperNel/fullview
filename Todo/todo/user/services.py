import typing as t

from ellar.di import injectable, singleton_scope
from ellar.core import Config
from ellar.common import HTTPException

from ..db.models import User
from ..db.database import get_session_maker



@injectable(scope=singleton_scope)
class UserService:
    def __init__(self, config: Config) -> None:
        session_maker = get_session_maker(config)
        self.db = session_maker()

    def create_user(self, user_data) -> t.Dict:
        print("ifff")
        if self.db.query(User).filter(User.email == user_data.email).first():
            raise HTTPException(status_code=400, detail=f"User with username {user_data.email} already exist")
        user = User(email=user_data.email,
                    first_name=user_data.first_name,
                    last_name=user_data.last_name,
                    )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_all_users(self) -> t.Dict:
        users = self.db.query(User).all()
        return users

    def get_user_by_id(self, user_id) -> t.Dict:
        user = self.db.query(User).filter(User.id == user_id).first()
        return user