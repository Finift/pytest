import pytest
import requests
from configuration import SERVICE_URL
import random
from src.generators.player import Player


@pytest.fixture
def get_player_generator():
    return Player()

@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42


@pytest.fixture()
def fix_data():
    """Return answer to ultimate question."""
    return ['BBG000C16SC2', 'BBG00Z3YMPH6', 'BBG001Y7R8L4', 'BBG000PSNF38', 'BBG000B9Y9C7']


@pytest.fixture()
def status_code():
    print('Code from fixture')
    return 200


@pytest.fixture()
def get_users():
    response = requests.get(SERVICE_URL)
    return response


# передать значения в фикстуру:
def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture()
def calculate():
    return _calculate


@pytest.fixture()
def make_number():
    print("I'm getting number")
    number = random.randrange(1, 1000, 5)
    yield
    print(f"Number at home {number}")
