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


a = Numbers([1, 2, 3, 4, 5, 6, 7])
print(a.summ())
print(a.average())
print(a.max())
print(a.min())

"""Задание 2
Создайте класс для числа. В классе должна быть реализована следующая функциональность:
■ Запись и чтение значения.
■ Перевод числа в восьмеричную систему исчисления.
■ Перевод числа в шестнадцатеричную систему исчисления.
■ Перевод числа в двоичную систему исчисления.
Протестируйте все возможности созданного класса
с помощью модульного тестирования(unittest)."""


class Number:

    def __init__(self, x):
        self.x = x

    def read_number(self):
        ...

    def save_number(self):
        ...

    def convert_number(self):
        ...



