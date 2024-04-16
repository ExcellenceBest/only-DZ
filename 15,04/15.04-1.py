"""Задание 1.
Создайте класс Circle (окружность). Для данного класса реализуйте
ряд перегруженных операторов: проверка на равенство площадей двух
окружностей (операция ==, !=), проверка сравнения площадей двух
окружностей (операции >, <,<=,>=)."""

from math import pi

class Circle:

    def __init__(self, radius: float):
        self._radius = self.validate_radius(radius)

    @staticmethod
    def validate_radius(radius):
        if not isinstance(radius, float):
            raise ValueError('Параметр radius числом с плавающей точкой')
        if radius < 0:
            raise ValueError('Параметр radius не может быть отрицательным числом')
        return radius

    @property
    def get_radius(self):
        return self._radius

    def area_figure(self):
        return round(pi*self._radius**2, 4)

    def __float__(self) -> float:
        return float(round(pi*self._radius**2, 4))

    def __eq__(self, other) -> bool:
        if isinstance(other, Circle):
            return float(self) == float(other)
        if isinstance(other, float):
            return self.area_figure() == other
        raise TypeError(f"'==' не поддерживается между типами Circle and {other.__class__.__name__}")

    def __ne__(self, other) -> bool:
        if isinstance(other, Circle):
            return float(self) != float(other)
        if isinstance(other, float):
            return self.area_figure() != other
        raise TypeError(f"'!=' не поддерживается между типами Circle and {other.__class__.__name__}")

    def __lt__(self, other) -> bool:
        if isinstance(other, Circle):
            return float(self) < float(other)
        if isinstance(other, float):
            return self.area_figure() < other
        raise TypeError(f"'<' не поддерживается между типами Circle and {other.__class__.__name__}")

    def __le__(self, other) -> bool:
        if isinstance(other, Circle):
            return float(self) <= float(other)
        if isinstance(other, float):
            return self.area_figure() <= other
        raise TypeError(f"'<=' не поддерживается между типами Circle and {other.__class__.__name__}")

    def __gt__(self, other) -> bool:
        if isinstance(other, Circle):
            return float(self) >= float(other)
        if isinstance(other, float):
            return self.area_figure() >= other
        raise TypeError(f"'>=' не поддерживается между типами Circle and {other.__class__.__name__}")


    def __ge__(self, other) -> bool:
        if isinstance(other, Circle):
            return float(self) > float(other)
        if isinstance(other, float):
            return self.area_figure() > other
        raise TypeError(f"'>' не поддерживается между типами Circle and {other.__class__.__name__}")

# c1 = Circle(1.1)
# c2 = Circle(1.2)
# print(c1 == c2)
# print(c1 <= c2)
# print(c1 < c2)
# print(c1 >= c2)
# print(c1 > c2)


"""    Задание 2.
Создайте класс Date, который будет содержать информацию о текущей
дате (день, месяц, год). Для данного класса реализуйте ряд перегруженных
операторов: проверка на равенство двух дат (операция ==, !=), проверка
сравнения двух дат (операции >, <,<=,>=)."""


from datetime import datetime, date

class Date:
    def __init__(self, day: int, month: int, year: int):
        self._day = self.validate_day(day)
        self._month = self.validate_month(month)
        self._year = self.validate_year(year)

    @staticmethod
    def validate_day(day):
        if not isinstance(day, int):
            raise ValueError('Параметр day должен быть целочисленным')
        if 31 < day < 1:
            raise ValueError('Параметр day вне диапазона 1-31')
        return day

    @staticmethod
    def validate_month(month):
        if not isinstance(month, int):
            raise ValueError('Параметр month должен быть целочисленным')
        if 12 < month < 1:
            raise ValueError('Параметр month вне диапазона 1-12')
        return month

    @staticmethod
    def validate_year(year):
        if not isinstance(year, int):
            raise ValueError('Параметр year должен быть целочисленным')
        return year

    def __int__(self) -> date:
        data = datetime(self._day, self._month, self._year)
        seconds = int(round(data.timestamp()))
        return seconds

    def __eq__(self, other) -> bool:
        if isinstance(other, Date):
            return int(self) == int(other)
        if isinstance(other, int):
            return int(self) == other
        raise TypeError(f"'==' не поддерживается между типами Date and {other.__class__.__name__}")

    def __ne__(self, other) -> bool:
        if isinstance(other, Date):
            return int(self) != int(other)
        if isinstance(other, int):
            return int(self) != other
        raise TypeError(f"'!=' не поддерживается между типами Date and {other.__class__.__name__}")

    def __lt__(self, other) -> bool:
        if isinstance(other, Date):
            return int(self) < int(other)
        if isinstance(other, int):
            return int(self) < other
        raise TypeError(f"'<' не поддерживается между типами Date and {other.__class__.__name__}")

    def __le__(self, other) -> bool:
        if isinstance(other, Date):
            return int(self) <= int(other)
        if isinstance(other, int):
            return int(self) <= other
        raise TypeError(f"'<=' не поддерживается между типами Date and {other.__class__.__name__}")

    def __gt__(self, other) -> bool:
        if isinstance(other, Date):
            return int(self) >= int(other)
        if isinstance(other, int):
            return int(self) >= other
        raise TypeError(f"'>=' не поддерживается между типами Date and {other.__class__.__name__}")

    def __ge__(self, other) -> bool:
        if isinstance(other, Date):
            return int(self) > int(other)
        if isinstance(other, int):
            return int(self) > other
        raise TypeError(f"'>' не поддерживается между типами Date and {other.__class__.__name__}")

# new = Date(2024, 4, 21)
# new1 = Date(2024, 4, 20)
# print(new == new1)
# print(new != new1)
# print(new < new1)
# print(new <= new1)
# print(new > new1)
# print(new >= new1)
