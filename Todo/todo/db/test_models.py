from todo.db.models import Routine, User

class TestModels:
    def test_user_model(self, db):
        user = User(id=1,
                    email="nel1@gmail.com",
                    first_name="nel",
                    last_name="uche",
                    is_active=True
                    )
        db.add(user)
        db.commit()
        db.refresh(user)
        assert user.email == "nel1@gmail.com"
        assert user.first_name == "nel"
        assert user.last_name == "uche"
        assert user.is_active == True


    def test_routine_model(self, db, create_user):
        routine = Routine(morning="workout", afternoon="sleep", night="code", status_completed=True, user_id=1)
        db.add(routine)
        db.commit()
        db.refresh(routine)
        assert routine.morning == "workout"
        assert routine.afternoon == "sleep"
        assert routine.night == "code"
        assert routine.status_completed == True
        assert routine.user_id == create_user.id

