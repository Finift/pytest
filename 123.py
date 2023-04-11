from mock import patch
import itertools  # важно: мы импортируем модуль, не сам метод
name = 'достаточно длинное имя'

with patch('itertools.permutations') as perm_mock:
    perm_mock.return_value = range(3)
    print(name)


