import unittest
from testing import Numbers
from testing import Number
from Testing2 import Fraction

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
    ...

