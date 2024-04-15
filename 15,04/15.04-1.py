"""Задание 1.
Создайте класс Circle (окружность). Для данного класса реализуйте
ряд перегруженных операторов: проверка на равенство площадей двух
окружностей (операция ==, !=), проверка сравнения площадей двух
окружностей (операции >, <,<=,>=)."""

from math import pi

class Circle:

    def __init__(self, radius: float):
        self._radius = radius

    @staticmethod
    def area_figure(radius):
        return round(pi*radius**2, 4)

    def __eq__(self, other) -> bool:
        if isinstance(other, Circle):
            return float(self) == float(other)
        if isinstance(other, int):
            return self.__get_seconds() == other
        raise TypeError(f"'==' не поддерживается между типами Time and {other.__class__.__name__}")

c1 = Circle(10)
c2 = Circle(10)
print(c1 == c2)
print(c1.area_figure(5))




#  """    Задание 2.
# Создайте класс Date, который будет содержать информацию о текущей
# дате (день, месяц, год). Для данного класса реализуйте ряд перегруженных
# операторов: проверка на равенство двух дат (операция ==, !=), проверка
# сравнения двух дат (операции >, <,<=,>=)."""
#

