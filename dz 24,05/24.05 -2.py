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
    
    def __init__(self, a: fractions, b: fractions) -> object:
        self.a = a
        self.b = b

    @classmethod
    def fract(cls, a, b):
        return cls(fractions.Fraction(a), fractions.Fraction(b))

    def __str__(self):
        return f'{fractions.Fraction(self.a, self.b)}'

    @staticmethod
    def addition():
        return

    @staticmethod
    def subtraction(a, b):
        return a.fract() - b.fract()

    @staticmethod
    def multiplication(a, b):
        return a.fract() * b.fract()

    @staticmethod
    def division(a, b):
        return a.fract() / b.fract()

    def __add__(self, other):
        ...

qwe = Fraction.fract(2, 9)
qwe1 = Fraction.fract(2, 9)
print(type(qwe))
print(type(qwe1))
a = Fraction(1, 1)
a = qwe + qwe1
print(a)
# fr = Fraction(6, 10)
# fr1 = Fraction(4, 10)
# fr2 = Fraction(5, 10)
# q = Fraction(1, 1)
# print(fr)
# print(fr1)
#
# print(q.addition(fr, fr1))
# print(q.subtraction(fr, fr1))
# print(q.multiplication(fr, fr1))
# print(q.division(fr, fr1))
# z = fr + fr1 + fr2

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

    ...

