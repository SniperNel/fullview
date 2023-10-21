from http import HTTPStatus
from ellar.testing import Test
from ..controllers import RoutineController
from ...db.models import Routine

class TestRoutineController:
    def setup_method(self):
        self.test_module = Test.create_test_module(controllers=[RoutineController])
        self.client = self.test_module.get_test_client()

    def test_get_list(self):
        response = self.client.get("/routine/all")
        assert response.status_code == 200
        data = response.json()
        assert data

    def test_get_list_status(self):
        response = self.client.get("/routine/status")
        assert response.status_code == 200
        data = response.json()
        assert data

    def test_update(self):
        detail = {
            "morning": "workout 2",
            "afternoon": "read 2",
            "night": "code",
        }
        response = self.client.put("/routine/6", json=detail)
        assert response.status_code == 200
        routine = Routine.query.get(id=6)
        assert routine.morning == detail["morning"]
        assert routine.afternoon == detail["afternoon"]
        assert routine.night == detail["night"]
        #data = response.json()
        #assert data

    def test_create(self):
        detail = {
            "morning": "trying from test",
            "afternoon": "cook",
            "night": "sleep"
        }
        response = self.client.post("/routine/create", json=detail)
        assert response.status_code == 200
        data = response.json()
        assert data == detail

    def test_delete(self):
        response = self.client.delete("/routine/21")
        assert response.status_code == HTTPStatus.NO_CONTENT