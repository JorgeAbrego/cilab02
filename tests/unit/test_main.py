from app.main import welcome


def test_welcome():
    result = welcome()
    assert isinstance(result, dict)
    assert result['message'] == "Welcome to the FastAPI project! :3"
