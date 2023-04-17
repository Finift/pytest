from forTest import sqrt_nums


def test_123():
    lst = [1, 7, 3, 5]
    assert sqrt_nums(lst) == [1, 9, 25, 49], 'Test failed'
