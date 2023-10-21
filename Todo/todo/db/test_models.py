from .models import Routine


def test_routine_model():
    routine = Routine(morning="workout", afternoon="sleep", night="code", status_completed="true", user_id=1)
    assert routine.morning == "workout"
    assert routine.afternoon == "sleep"
    assert routine.night == "code"
    assert routine.status_completed == "true"
    assert routine.user_id == 1