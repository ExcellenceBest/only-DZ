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
    def __init__(self, point_of_reference: list, side: int):
        self.point_of_reference = point_of_reference
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4

    def save(self):
        square = open('square', 'w', encoding='utf-8')
        square.write()
        square.close()

    def load(self):
        ...

square1 = Square([2, 2], 5)

class Rectangle(Shape):
    ...


class Circle(Shape):
    ...


class Ellipse(Shape):
    ...

def manipulation():
    area1 = square1.area()
    perimeter1 = square1.perimeter()
    print(area1, perimeter1)

manipulation()
