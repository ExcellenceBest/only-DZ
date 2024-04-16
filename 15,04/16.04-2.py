"""Задание 1
Создайте класс Flat (квартира). Для данного класса реализуйте ряд
перегруженных операторов: проверка на равенство площадей квартир
(операция == и !=), сравнение двух квартир по площади (операции >, <,
<=, >=).
Создайте класс контейнер ApartmentHouse (многоквартирный дом).
Атрибутом данного класса должен быть список объектов класса Flat.
Реализуйте в классе необходимые методы для работы с
последовательностями. Каждый новый дом по умолчанию имеет 10 этажей.
Продемонстрируйте работу с классом на примере."""

# class Flat:
#
#     def __init__(self, area_apartment: float):
#         self._area_apartment = area_apartment
#
#     @property
#     def area_apartment(self):
#         return self._area_apartment
#
# flat1 = Flat(1)
# flat2 = Flat(2)
# flat3 = Flat(3)
# flat4 = Flat(4)
# flat5 = Flat(5)
# flat6 = Flat(6)
# flat7 = Flat(7)
# flat8 = Flat(8)
# flat9 = Flat(9)
# flat10 = Flat(10)
# flat11 = Flat(11)
# flats = [flat1, flat2, flat3, flat4, flat5, flat6, flat7, flat8, flat9, flat10]
#
# class ApartmentHouse:
#
#     def __init__(self, flatses: list[Flat], floor: int = 10):
#         self._flats: list[Flat] = flatses
#         self._floor = floor
#
#     @property
#     def get_floor(self):
#         return self._floor
#
#
# house = ApartmentHouse(flats)
# print(house)


class Flat:
    def __init__(self, number, floor, area):
        self.number = number
        self.floor = floor
        self.area = area

    def __str__(self):
        return f"Квартира № {self.number}, этаж: {self.floor}, Площадь: {self.area} Кв.М."

class ApartmentHouse:
    def __init__(self, floors=10):
        self.flats = []
        for floor in range(floors):
            for i in range(1, 3): # Предположим, что на каждом этаже есть 3 квартиры
                self.flats.append(Flat(i, floor + 1, 60)) # Все квартиры имеют площадь 60 кв. м

    def print_flats(self):
        for flat in self.flats:
            print(flat)

# Создаем объект многоквартирного дома
house = ApartmentHouse()

# Выводим информацию о всех квартирах
house.print_flats()
