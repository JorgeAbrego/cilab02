# import pytest
# from app.api.v1.endpoints.random import hello_world
from app.api.v1.endpoints.random import generate_integer
from app.api.v1.endpoints.random import generate_float


# @pytest.mark.asyncio(loop_scope="function")
# async def test_hello_world():
#     # Se utiliza 'await' para llamar a la función async
#     result = await hello_world()
#     assert isinstance(result, dict)
#     assert result['message'] == "Welcome to Random Generator - V1"


def test_generate_integer():
    result = generate_integer()
    assert isinstance(result, int)
    assert 0 <= result <= 100


def test_generate_float():
    result = generate_float()
    assert isinstance(result, float)
    assert 0 <= result <= 100
