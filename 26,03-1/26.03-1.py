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
        return f'{self.side ** 2} {self.__unit_of_measurement}'

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

square1 = Square('Квадрат', 'Кв. См', [2, 2], 5)
print(square1.load('square.txt'))



class Rectangle(Shape):
    ...


class Circle(Shape):
    ...


class Ellipse(Shape):
    ...

def manipulation():
    square1.area()
    square1.perimeter()
    square1.save()

manipulation()
