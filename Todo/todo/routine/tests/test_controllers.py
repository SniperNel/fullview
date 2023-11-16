from ellar.di import ProviderConfig

from ellar.testing import Test, TestClient
from ..controllers import RoutineController
from ..services import RoutineDB


class TestRoutineController:
    def setup_method(self):
        self.test_module = Test.create_test_module(controllers=[RoutineController],
                                                   providers=[ProviderConfig(RoutineDB, use_class=RoutineDB)])
        self.client: TestClient = self.test_module.get_test_client()


    def test_create(self, db, create_user):
        detail = {
            "morning": "trying from test",
            "afternoon": "cook",
            "night": "sleep",
            "status_completed": False,
            "user_id": create_user.id
        }
        response = self.client.post("/routine/create", json=detail)
        assert response.status_code == 200
        data = response.json()
        assert data
        assert data["morning"] == detail["morning"]
        assert data["afternoon"] == detail["afternoon"]
        assert data["night"] == detail["night"]


    def test_get_list(self, db, routine):
        user_id = 1
        response = self.client.get(f"/routine/all/{user_id}")
        data = response.json()
        assert response.status_code == 200
        assert data
        print(data)

    def test_get_list_status(self, db, routine):
        response = self.client.get("/routine/status/1?status_completed=false")
        assert response.status_code == 200
        data = response.json()
        assert data

    def test_update(self, db, routine):
        detail_update = {
            "id": 1,
            "morning": "workout 2",
            "afternoon": "read 2",
            "night": "code",
            "status_completed": False,
            "user_id": 1
        }
        response = self.client.put(f"/routine/{routine.user_id}/{routine.id}", json=detail_update)
        assert response.status_code == 200
        data = response.json()
        assert data["morning"] == detail_update["morning"]
        assert data["afternoon"] == detail_update["afternoon"]
        assert data["night"] == detail_update["night"]
        assert data["status_completed"] == detail_update["status_completed"]
        assert data["id"] == detail_update["id"]


    def test_delete(self, db, routine):
        response = self.client.delete(f"/routine/{routine.user_id}/{routine.id}")
        assert response.status_code == 200
        data = response.json()
        assert data == {}