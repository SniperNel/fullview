import pytest
from ...conftest import temp_dp
from ellar.testing import Test

from todo.user.controllers import UserController



class TestUserController:
    # def setup_method(self):
    #     self.test_module = Test.create_test_module(controllers=[UserController])
    #     self.client = self.test_module.get_test_client()

    def test_user_get(temp_dp):
        response = temp_dp.get("/user/")
        assert response.status_code == 200
        data = response.json()
        assert data

    def test_user_create(self, temp_dp):
        data = {
            "id": 1,
            "email": "eze@gmail.com",
            "first_name": "trial",
            "last_name": "uche",
            "is_active": True,
            "created_date": "2023-10-24T11:19:13.725Z"
        }
        response = self.client.post("/user/add", json=data)
        assert response.status_code == 200
        detail = response.json()
        assert detail

    def test_get_user_id(self, temp_dp):
        user_id = 1
        response = self.client.get(f"/user/{user_id}")
        assert response.status_code == 200
        assert response.json


