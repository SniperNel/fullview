from ellar.di import ProviderConfig

from ellar.testing import Test, TestClient
from ..controllers import RoutineController
from ..services import RoutineDB


class TestRoutineController:
    def setup_method(self):
        self.test_module = Test.create_test_module(controllers=[RoutineController],
                                                   providers=[ProviderConfig(RoutineDB, use_class=RoutineDB)])
        self.client: TestClient = self.test_module.get_test_client()


    def test_create(self, db):
        detail = {
            "morning": "trying from test",
            "afternoon": "cook",
            "night": "sleep",
            "status_completed": False,
            "user_id": 1
        }
        response = self.client.post("/routine/create", json=detail)
        assert response.status_code == 200
        data = response.json()
        assert data
        assert data["morning"] == detail["morning"]
        assert data["afternoon"] == detail["afternoon"]
        assert data["night"] == detail["night"]


    def test_get_list(self, db):
        user_id = 1
        response = self.client.get(f"/routine/all/{user_id}")
        data = response.json()
        assert response.status_code == 200
        assert data
        print(data)

    def test_get_list_status(self, db):
        response = self.client.get("/routine/status/1?status_completed=false")
        assert response.status_code == 200
        data = response.json()
        assert data

    def test_update(self, db):
        detail_update = {
            "morning": "workout 2",
            "afternoon": "read 2",
            "night": "code",
        }
        response = self.client.patch("/routine/1?user_id=1", json=detail_update)
        assert response.status_code == 200

        data = response.json()
        print("for update", data)
        assert data


    def test_delete(self, db):
        response = self.client.delete("/routine/1?user_id=1")
        assert response.status_code == 204