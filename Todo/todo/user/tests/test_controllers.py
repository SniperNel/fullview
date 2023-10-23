from http import HTTPStatus
from ellar.testing import Test
from ..controllers import UserController
from ...routine.controllers import RoutineController
from ...db.models import User

class TestUserController:
    def setup_method(self):
        self.test_module = Test.create_test_module(controllers=[UserController, RoutineController])
        self.client = self.test_module.get_test_client()

    # def test_create_user(self):
    #     detail = {
    #         "email": "nel@gmail.com",
    #         "first_name": "nel",
    #         "last_name": "uche",
    #     }
    #     response = self.client.post("/user/add", json=detail)
    #     assert response.status_code == 200
    #     data = response.json()
    #     assert data == detail

    def test_user_list(self):
        response = self.client.get("/user")
        assert response.status_code == 200
        data = response.json()
        assert data
