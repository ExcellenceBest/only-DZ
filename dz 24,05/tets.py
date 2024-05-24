import unittest
from testing import Numbers


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
