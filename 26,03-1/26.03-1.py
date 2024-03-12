"""Задание 1
Создайте базовый абстрактный класс Shape для хранения методов
плоских фигур: area, perimeter, save, load. Определите следующие производные
классы:
Square — квадрат, который характеризуется координатами левого
верхнего угла и длиной стороны;
Rectangle — прямоугольник с заданными координатами верхнего
левого угла и размерами;
Circle — окружность с заданными координатами центра и радиусом;
Ellipse — эллипс с заданными координатами верхнего угла описанного
вокруг него прямоугольника со сторонами, параллельными осям координат,и
размерами этого прямоугольника.
Создайте список фигур. Напишите функцию, которая сохраняет
каждую фигуру в отдельный файл, загружает фигуру из файла и отображает
информацию о каждой из фигур, включая площадь и периметр."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError

    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def load(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, name: str, unit_of_measurement: str, point_of_reference: list, side: int):
        self.__name = name
        self.__unit_of_measurement = unit_of_measurement
        self.point_of_reference = point_of_reference
        self.side = side

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def unit_of_measurement(self):
        return self.__unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, unit_of_measurement):
        self.__unit_of_measurement = unit_of_measurement


    def area(self):
        return f'{self.side ** 2} Кв.{self.__unit_of_measurement}'

    def perimeter(self):
        return f'{self.side * 4} {self.__unit_of_measurement}'

    def save(self):
        lst = [('Фигура', square1.__name), ('Площадь фигуры', square1.area()), ('Периметр', square1.perimeter())]
        doc1 = ''
        for i in lst:
            doc1 += str(i[0] + ':' + '\t' + str(i[1])) + '\n'
        square = open('square', 'w', encoding='utf-8')
        square.write(str(doc1))
        square.close()

    def load(self,path: str) -> str:
        with open(path, 'r', encoding='utf-8') as file:
            info_of_figure = file.read()
        return info_of_figure

square1 = Square('Квадрат', 'См', [2, 2], 5)


class Rectangle(Shape):
    ...


class Circle(Shape):
    def __init__(self, name: str, unit_of_measurement: str, point_of_reference: list, radius: int):
        self.__name = name
        self.__unit_of_measurement = unit_of_measurement
        self.__point_of_reference = point_of_reference
        self.__radius = radius

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def unit_of_measurement(self):
        return self.__unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, unit_of_measurement):
        self.__unit_of_measurement = unit_of_measurement

    def area(self):
        return f'{round(self.__radius ** 2 * pi), 2} {self.__unit_of_measurement}'

    def perimeter(self):
        return f'{round(2 * pi * self.__radius), 2} {self.__unit_of_measurement}'

    def save(self):
        lst = [('Фигура', round1.__name), ('Площадь фигуры', round1.area()), ('Периметр', round1.perimeter())]
        doc1 = ''
        for i in lst:
            doc1 += str(i[0] + ':' + '\t' + str(i[1])) + '\n'
        round = open('round', 'w', encoding='utf-8')
        round.write(str(doc1))
        round.close()

    def load(self,path: str) -> str:
        with open(path, 'r', encoding='utf-8') as file:
            info_of_figure = file.read()
        return info_of_figure


round1 = Circle('Окружность', 'См', [6, 6], 4)


class Ellipse(Shape):
    ...

def manipulation():
    square1.area()
    square1.perimeter()
    square1.save()
    print(square1.load('square.txt'))
    round1.area()
    round1.perimeter()
    round1.save()
    print(round1.load("round.txt"))

manipulation()

