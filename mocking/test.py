# from unittest import TestCase
# from main import Calculator
#
# class TestCalculator(TestCase):
#     def setUp(self):
#         self.calc = Calculator()
#
#     def test_sum(self):
#         answer = self.calc.sum(2, 4)
#         self.assertEqual(answer, 6)
from unittest import TestCase
from unittest.mock import patch


# class TestCalculator(TestCase):
#     @patch('main.Calculator.sum', return_value=9)
#     def test_sum(self, sum):
#         self.assertEqual(sum(2, 3), 9)

# Теперь запустим ф-цию калькулятора без задержек в 10 сек, для этого используем side_effect:

def mock_sum(a, b):
    # mock sum function without the long running time.sleep
    return a + b

class TestCalculator(TestCase):
    @patch('main.Calculator.sum', side_effect=mock_sum)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(7, 3), 10)
