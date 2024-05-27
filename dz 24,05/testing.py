"""Задание 1
Создайте класс, содержащий набор целых чисел.
Функциональность:
■ Сумма элементов набора.
■ Среднеарифметическое элементов набора.
■ Максимум из элементов набора.
■ Минимум из элементов набора.
Протестируйте все возможности созданного класса
с помощью модульного тестирования(unittest)."""


class Numbers:

    def __init__(self, numbers: list):
        self._numbers = numbers

    def __str__(self):
        return f'{self._numbers}'

    def summ(self):
        return sum(self._numbers)

    def average(self) -> float:
        a = sum(self._numbers) / len(self._numbers)
        return a

    def max(self) -> int:
        return max(self._numbers)

    def min(self) -> int:
        return min(self._numbers)


# a = Numbers([1, 2, 3, 4, 5, 6, 7])
# print(a.summ())
# print(a.average())
# print(a.max())
# print(a.min())

"""Задание 2
Создайте класс для числа. В классе должна быть реализована следующая функциональность:
■ Запись и чтение значения.
■ Перевод числа в восьмеричную систему исчисления.
■ Перевод числа в шестнадцатеричную систему исчисления.
■ Перевод числа в двоичную систему исчисления.
Протестируйте все возможности созданного класса
с помощью модульного тестирования(unittest)."""


class Number:

    @staticmethod
    def read_number(path: str):
        with open(path, 'r', encoding='utf-8') as file:
            number = int(file.read())
        return number

    @staticmethod
    def save_number(number, path: str):
        file1 = open(path, 'w', encoding='utf-8')
        file1.write(str(number))
        file1.close()

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


a = Number()
a.save_number(100, 'xxx.txt')
print(a.read_number('file.txt'))
#print(a.universal_convert(150, 8))
print(a.convert_8(100))
print(a.convert_2(100))
print(a.convert_16(100))
