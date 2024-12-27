from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_random_endpoints_integration():
    # Test welcome endpoint
    # response = client.get("/v1/random/")
    # assert response.status_code == 200
    # assert response.json() == {"message": "Welcome to Random Generator - V1"}

    # Test random integer generation
    response = client.get("/v1/random/int/")
    assert response.status_code == 200
    random_int = response.json()
    assert isinstance(random_int, int)
    assert 0 <= random_int <= 100

    # Test random float generation
    response = client.get("/v1/random/float/")
    assert response.status_code == 200
    random_float = response.json()
    assert isinstance(random_float, float)
    assert 0 <= random_float <= 100
