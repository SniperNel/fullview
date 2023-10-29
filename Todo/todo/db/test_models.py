from .models import Routine, User


# def test_routine_model():
#     routine = Routine(morning="workout", afternoon="sleep", night="code", status_completed="true", user_id=1)
#     assert routine.morning == "workout"
#     assert routine.afternoon == "sleep"
#     assert routine.night == "code"
#     assert routine.status_completed == "true"
#     assert routine.user_id == 1
#
# def test_user_model():
#     user = User(email="nel@gmail.com",
#                 first_name="nel",
#                 last_name="uche",
#                 is_active="true"
#                 )
#     assert user.email == "nel@gmail.com"
#     assert user.first_name == "nel"
#     assert user.last_name == "uche"
#     assert user.is_active == "true"