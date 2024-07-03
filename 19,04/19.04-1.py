"""Задание 1.
Создайте класс «Число», которое хранит его значение и информацию о
системе счисления. Создайте несколько экземпляров данного класса.
Задание 2.
Создайте класс «Калькулятор СС». В классе должна быть реализована
следующая функциональность:
– Перевод числа в восьмеричную систему счисления.
– Перевод числа в шестнадцатеричную систему счисления.
– Перевод числа в двоичную систему счисления.
– Перевод числа в десятичную систему счисления.
–Сложение двух чисел в разных системах счисления через обычный
арифметический оператор и составное присваивание. Результат сложения
записать в СС левого операнда."""


class Number:

    @staticmethod
    def convert_8(x):
        result = ''
        while x > 0:
            result += str(x % 8)
            x = x // 8
        result = int(result[::-1])
        return result

    @staticmethod
    def convert_16(x):
        result = ''
        while x > 0:
            result += str(x % 16)
            x = x // 16
        result = int(result[::-1])
        return result

    @staticmethod
    def convert_2(x):
        result = ''
        while x > 0:
            result += str(x % 2)
            x = x // 2
        result = int(result[::-1])
        return result

# Универсальный конвертер, вторая переменная - система исчисления
#     @staticmethod
#     def universal_convert(x, y):
#         result = ''
#         while x > 0:
#             result += str(x % y)
#             x = x // y
#         result = result[::-1]
#         return result