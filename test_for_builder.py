import pytest
from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization



# Проверили работоспособность со всеми видами статусов
@pytest.mark.parametrize("status", [status.value for status in Statuses])
def test_something(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


# с разными балансами
@pytest.mark.parametrize("balance_value", ["100", "-10", "hgjh"])
def test_something2(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())


# проверили работоспособность без каждого из параметров
@pytest.mark.parametrize("delete_key", ["account status", "balance", "localize", "avatar"])
def test_something1(delete_key, get_player_generator):
    obj_to_send = get_player_generator.build()
    del obj_to_send[delete_key]
    print(obj_to_send)


# Добавили параметр и изменили локализацию на франц
def test_something3(get_player_generator):
    obj_to_send = get_player_generator.update_inner_generator('localize', PlayerLocalization('fr_FR').set_number(17)).build()
    print(obj_to_send)
