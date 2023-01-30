import pytest


@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42


@pytest.fixture()
def fix_data():
    """Return answer to ultimate question."""
    return ['BBG000C16SC2', 'BBG00Z3YMPH6', 'BBG001Y7R8L4', 'BBG000PSNF38', 'BBG000B9Y9C7']


