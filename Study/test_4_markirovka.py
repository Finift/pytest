import pytest


@pytest.mark.development
@pytest.mark.parametrize('f_value, s_value, result', [
    (0, 0, 0),
    (-1, 5, 4),
    (1, -5, -4),
    (7, 10, 17),
    (-100, -50, -150),
    (0, 15, 15),
    (-100, 0, -100),
    ("f", 14, None),
    (5, 17.8, None),
    ("d", "q", None),
    (" ", 5, None)
])
def test_calculate(f_value, s_value, result, calculate):
    # assert calculate(0, 0) == 0
    # assert calculate(-1, 5) == 4
    # assert calculate(1, -5) == -4
    # assert calculate(7, 10) == 17
    # assert calculate(-100, -50) == -150
    # assert calculate(0, 15) == 15
    # assert calculate(-100, 0) == -100
    # assert calculate("f", 14) == None
    # assert calculate(5, 17.8) == None
    # assert calculate("d", "q") == None
    # assert calculate(" ", 5) == None
    #Вот это всё заменяем параметризированным тестом:
    assert calculate(f_value, s_value) == result
