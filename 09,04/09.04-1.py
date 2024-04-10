
from abc import ABC, abstractmethod
"""Задание 1.
Создайте программу, имитирующую многоквартирный дом. Необходимо
иметь классы «Человек», «Квартира», «Дом». Класс «Квартира» содержит
список объектов класса «Человек». Класс «Дом» содержит список объектов
класса «Квартира». Реализуйте:
 Вывод информации о всех жильцах определенной квартиры
 Вывод информации о всех квартирах в определенном доме"""

# FIXME: А зачем нам этот класс?
class Info(ABC):
    @abstractmethod
    def get_info(self):
        ...


# FIXME: класс Human точно будет наследником класса Info?
class Human(Info):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    # FIXME: если оставляем get_info то убираем __str__ и наоборот
    def get_info(self):
        # FIXME: нужен более иинформативный вывод Имя: ... Возраст: ...
        return [self._name, self._age]


    def __str__(self):
        return "% s: % s" % (self._name, self._age)

    # FIXME: зачем нам repr?
    def __repr__(self):
        return "% s: % s" % (self._name, self._age)


human1 = Human('Папа', 40)
human2 = Human('Мама', 35)
human3 = Human('Саша', 15)
human4 = Human('Папа', 25)
human5 = Human('Мама', 25)
human6 = Human('Мама', 55)
print(human3.get_info())

family1 = [human1, human2, human3]
family2 = [human4, human5]
family3 = [human6]

# FIXME: Flat точно должен быть наследником класса Info?
class Flat(Info):
    def __init__(self, number: int, family: list[Human]):
        self._number = number
        self._family: list[Human] = family

    @property
    def family(self):
        return self._family

    @property
    def number(self):
        return self._number

    # FIXME: зачем нам repr?
    def __repr__(self):
        return "Кв. № % s: % s" % (self._number, self._family)

    def __str__(self):
        return "Квартира № % s: Живут: % s" % (self._number, self._family)

    # FIXME: оставить либо get_info, либо str и подробно расписать вывод
    def get_info(self):
        return [self._number, self.family]


flat1 = Flat(1, family1)
print(flat1)
flat2 = Flat(2, family2)
flat3 = Flat(1, family3)
flats = [flat3, flat2, flat1]

# FIXME: House точно должен быть наследником класса Info?
class House(Info):
    def __init__(self, number: int, flats:[Flat]):
        self._number = number
        self._flats: list[Flat] = flats

    # FIXME: оставить либо str либо get_info и расписать подробный вывод
    def __str__(self):
        return "Дом № % s: % s" % (self._number, self._flats)

    def get_info(self):
        return self._number, self._flats



house1 = House(2, flats)
# TODO: Как добавить другие квартиры в этот дом?
house2 = House(3, flat3)
print('________________________')
print(house1)
print('________________________')
print(house2)
print('________________________')
print(flat2.get_info())
print(flat3.get_info())
