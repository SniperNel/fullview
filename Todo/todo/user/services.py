from ellar.di import injectable, singleton_scope

from ..db.models import User
from ..db.database import SessionLocal


@injectable(scope=singleton_scope)
class UserService:
    def __init__(self) -> None:
        self.db = SessionLocal()

    def create_user(self, user_data):
        user = User(email=user_data.email,
                    first_name=user_data.first_name,
                    last_name=user_data.last_name,
                    )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_all_users(self):
        users = self.db.query(User).all()
        return users

    def get_user_by_id(self, user_id):
        user = self.db.query(User).filter(User.id == user_id).first()
        return user