"""Задание 1
Создайте класс по работе с дробями. В классе должна
быть реализована следующая функциональность:
■ Сложение дробей;
■ Вычитание дробей;
■ Умножение дробей;
■ Деление дробей.
Протестируйте все возможности созданного класса
с помощью модульного тестирования (unittest)."""
import fractions


class Fraction:
    
    def __init__(self, a: fractions, b: fractions):
        self.a = a
        self.b = b

    @staticmethod
    def fract(a, b):
        return fractions.Fraction(a, b)

    def __str__(self):
        return f'{fractions.Fraction(self.a, self.b)}'

    @staticmethod
    def addition(a, b):
        return a.fract() + b.fract()

    @staticmethod
    def subtraction(a, b):
        return a.fract() - b.fract()

    @staticmethod
    def multiplication(a, b):
        return a.fract() * b.fract()

    @staticmethod
    def division(a, b):
        return a.fract() / b.fract()


# qwe = Fraction.fract(2, 9)
# qwe1 = Fraction.fract(2, 9)
# print(qwe)
# print(qwe1)
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


a = Calculator()
print(a.degree(2, 10))
q = a.percent(200, 24)
print(q)
print(a.max(23, 14))
