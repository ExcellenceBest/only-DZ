import fractions
import unittest
from testing import Numbers
from testing import Number
from Testing2 import Calculator

class TestNumbers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.a = list()

    def setUp(self):
        self.numbers = Numbers([1, 2, 3, 4, 5, 6, 7])

    def test_summ(self):
        self.assertEqual(self.numbers.summ(), 28)

    def test_average(self):
        self.assertEqual(self.numbers.average(), 4.0)

    def test_max(self):
        self.assertEqual(self.numbers.max(), 7)

    def test_min(self):
        self.assertEqual(self.numbers.min(), 1)

    def tearDown(self):
        print('test ok')


if __name__ == '__main__':
    unittest.main()


class TestNumber(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.a = str()

    def setUp(self):
        self.number = Number

    def test_read_number(self):
        self.assertEqual(self.number.read_number('file.txt'), 150)

    def test_save_number(self):
        self.assertEqual(100, self.number.read_number('xxx.txt'))

    def test_convert_8(self):
        self.assertEqual(self.number.convert_8(100), 144)

    def test_convert_16(self):
        self.assertEqual(self.number.convert_16(100), 64)

    def test_convert_2(self):
        self.assertEqual(self.number.convert_2(100), 1100100)

    def tearDown(self):
        print('test ok')


if __name__ == '__main__':
    unittest.main()


class TestFraction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.a = fractions.Fraction
        cls.b = fractions.Fraction

    def setUp(self):
        self.fraction = fractions.Fraction

    def test_addition(self):
        ...


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.a = int()
        cls.b = int()

    def setUp(self):
        self.calculator = Calculator

    def test_addition(self):
        self.assertEqual(self.calculator.addition(20, 40), 60)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(88, 45), 43)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(25, 25), 625)

    def test_division(self):
        self.assertEqual(self.calculator.division(96, 16), 6)

    def test_max(self):
        self.assertEqual(self.calculator.max(24, 14), 24)

    def test_min(self):
        self.assertEqual(self.calculator.min(2, 14), 2)

    def test_percent(self):
        self.assertEqual(self.calculator.percent(200, 25), 50)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 13), 8192)

    def tearDown(self):
        print('test ok')


if __name__ == '__main__':
    unittest.main()
