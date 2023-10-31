from ellar.di import ProviderConfig

from todo.user.controllers import UserController
from ..services import UserService
from ellar.testing import Test, TestClient



class TestUserController:
    def setup_method(self):
        self.test_module = Test.create_test_module(controllers=[UserController], providers=[ProviderConfig(UserService)])
        self.client: TestClient = self.test_module.get_test_client()

    def test_user_create(self, db):
        data = {
            "email": "eze2@gmail.com",
            "first_name": "nel",
            "last_name": "uche",
            "is_active": True,
        }
        response = self.client.post("/user/add", json=data)
        assert response.status_code == 200
        detail = response.json()
        assert detail["id"]
        assert detail["created_date"]
        assert detail["email"] == data["email"]
        assert detail["first_name"] == data["first_name"]
        assert detail["last_name"] == data["last_name"]

    def test_user_get(self, db):
        response = self.client.get("/user/")
        assert response.status_code == 200
        data = response.json()
        print(data)
        assert data

    def test_get_user_id(self, db):
        user_id = 1
        response = self.client.get(f"/user/{user_id}")
        assert response.status_code == 200
        user = response.json()
        assert user
        print(user)


