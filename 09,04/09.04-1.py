"""Задание 1.
Создайте программу, имитирующую многоквартирный дом. Необходимо
иметь классы «Человек», «Квартира», «Дом». Класс «Квартира» содержит
список объектов класса «Человек». Класс «Дом» содержит список объектов
класса «Квартира». Реализуйте:
 Вывод информации о всех жильцах определенной квартиры
 Вывод информации о всех квартирах в определенном доме"""

class Human:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

human1 = Human('Папа', 40)
human2 = Human('Мама', 35)
human3 = Human('Ребенок', 15)

family1 = [human1, human2, human3]

class Flat:
    def __init__(self, number: int):
        self._number = number
        self._flat: list[Human] = []

flat1 = Flat(1)
flat2 = Flat(2)
flat3 = Flat(3)
flat4 = Flat(4)
flats = [flat4, flat3, flat2, flat1]

class House:
    def __init__(self):
        self._house: list[Flat] = []

    def house_info(self, flat: list):
        for i in flat:
            print(i.Flat._number)




