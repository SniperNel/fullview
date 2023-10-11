from .models import Routine


def test_routine_model():
    routine = Routine(morning="workout", afternoon="sleep", night="code")
    assert routine.morning == "workout"
    assert routine.afternoon == "sleep"
    assert routine.night == "code"