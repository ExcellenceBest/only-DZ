"""Задание 1.
Создайте класс Flat (квартира). Для данного класса реализуйте ряд
перегруженных операторов: проверка на равенство площадей квартир
(операция == и !=), сравнение двух квартир по площади (операции >, <,
<=, >=).
Создайте класс контейнер ApartmentHouse (многоквартирный дом).
Атрибутом данного класса должен быть список объектов класса Flat.
Реализуйте в классе необходимые методы для работы с
последовательностями. Каждый новый дом по умолчанию имеет 10 этажей.
Продемонстрируйте работу с классом на примере."""


class Flat:

    def __init__(self, number: int, square: float):
        self._square = self.validate_square(square)
        self._number = self.validate_number(number)

    def __str__(self):
        return (f'Номер квартиры: {self._number}, '
                f'Площадь: {self._square} кв.м.')

    @staticmethod
    def validate_number(number):
        if not isinstance(number, int):
            raise ValueError('Параметр number не является целочисленным')
        if number < 0:
            raise ValueError('Параметр number не может быть отрицательным')
        return number

    @staticmethod
    def validate_square(square):
        if not isinstance(square, float):
            raise ValueError('Параметр square не является числом с плавающей точкой')
        if square < 0:
            raise ValueError('Параметр square не может быть отрицательным')
        return square

    def get_square(self):
        return self._square

    def get_number(self):
        return self._number


    def __eq__(self, other) -> bool:
        if isinstance(other, Flat):
            return self.get_square() == other
        if isinstance(other, float):
            return self.get_square() == other
        raise TypeError(f"'==' не поддерживается между типами Flat and {other.__class__.__name__}")

    def __ne__(self, other) -> bool:
        if isinstance(other, Flat):
            return self.get_square() != other
        if isinstance(other, float):
            return self.get_square() != other
        raise TypeError(f"'!=' не поддерживается между типами Flat and {other.__class__.__name__}")

    def __lt__(self, other) -> bool:
        if isinstance(other, Flat):
            return self.get_square() < other
        if isinstance(other, float):
            return self.get_square() < other
        raise TypeError(f"'<' не поддерживается между типами Flat and {other.__class__.__name__}")

    def __le__(self, other) -> bool:
        if isinstance(other, Flat):
            return self.get_square() <= other
        if isinstance(other, float):
            return self.get_square() <= other
        raise TypeError(f"'<=' не поддерживается между типами Flat and {other.__class__.__name__}")

    def __gt__(self, other) -> bool:
        if isinstance(other, Flat):
            return self.get_square() >= other
        if isinstance(other, float):
            return self.get_square() >= other
        raise TypeError(f"'>=' не поддерживается между типами Flat and {other.__class__.__name__}")


    def __ge__(self, other) -> bool:
        if isinstance(other, Flat):
            return self.get_square() > other
        if isinstance(other, float):
            return self.get_square() > other
        raise TypeError(f"'>' не поддерживается между типами Flat and {other.__class__.__name__}")

flat = Flat(1, 48.0)
flat2 = Flat(2, 20.5)
flat3 = Flat(3, 36.0)
flat4 = Flat(4, 30.0)
flat5 = Flat(5, 43.0)
flat6 = Flat(6, 44.6)
flat7 = Flat(7, 43.0)
flat8 = Flat(8, 80.4)
flats = [flat, flat8, flat4, flat7, flat6, flat5, flat3, flat2]


class ApartmentHouse:

    def __init__(self, flats: list[Flat], floors=10):
        self._flat: [] = flats
        self._floors = floors


    def add_flat(self, flats: list[Flat]):
        flats.append(self)

    @staticmethod
    def get_flat_square(item):
        return f'Площадь квартиры {item.get_number()} составляет {Flat.get_square(item)} кв.м.'

    @staticmethod
    def get_all_flats():
        for i in flats:
            print(i)


print(flat8 == flat4)  # False
print(flat6 != flat7)  # True
print(flat3 > flat5)    # False
print(flat4 < flat)     # True
print(flat8 >= flat2)   # True
print(flat7 <= flat4)   # False
ApartmentHouse.get_all_flats()
flat9 = Flat(9, 111.8)
ApartmentHouse.add_flat(flat9, flats)
ApartmentHouse.get_all_flats()
print(ApartmentHouse.get_flat_square(flat7))
print(ApartmentHouse.get_flat_square(flat9))

