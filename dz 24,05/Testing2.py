"""Задание 1
Создайте класс по работе с дробями. В классе должна
быть реализована следующая функциональность:
■ Сложение дробей;
■ Вычитание дробей;
■ Умножение дробей;
■ Деление дробей.
Протестируйте все возможности созданного класса
с помощью модульного тестирования (unittest)."""
from fractions import Fraction


class NewFraction:
    
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    @staticmethod
    def fract(a: int, b: int) -> Fraction:
        return Fraction(a, b)

    def __str__(self):
        return f'{Fraction(self.a, self.b)}'

    @staticmethod
    def addition(a: Fraction, b: Fraction):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b


# qwe = NewFraction.fract(5, 10)
# qwe1 = NewFraction.fract(3, 10)
# x = qwe + qwe1
# x2 = qwe - qwe1
# x3 = qwe * qwe1
# x4 = qwe / qwe1
# print(x, x2, x3, x4)


""" Задание 2
Создайте класс Калькулятор. В классе должна быть
реализована следующая функциональность:
■ Сложение двух чисел;
■ Вычитание двух чисел;
■ Умножение двух чисел;
■ Деление двух чисел;
■ Максимум из двух чисел;
■ Минимум из двух чисел;
■ Процент числа;
■ Возведение числа в степень.
Протестируйте все возможности созданного класса с
помощью модульного тестирования (unittest)"""


class Calculator:

    def __init__(self, a=None, b=None):
        self.a = None
        self.b = None

    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b

    @staticmethod
    def max(a, b):
        return max(a, b)

    @staticmethod
    def min(a, b):
        return min(a, b)

    @staticmethod
    def percent(a, b):
        return (a / 100) * b

    @staticmethod
    def degree(a, b):
        return a ** b


# aa = Calculator()
# print(aa.degree(2, 10))
# q = aa.percent(200, 24)
# print(q)
# print(aa.max(23, 14))
