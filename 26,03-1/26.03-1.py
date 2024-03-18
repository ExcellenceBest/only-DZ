"""Задание 1.
Создайте базовый абстрактный класс Shape для хранения методов
плоских фигур: area, perimeter, save, load. Определите следующие производные
классы:
Square — квадрат, который характеризуется координатами левого
верхнего угла и длиной стороны;
Rectangle — прямоугольник с заданными координатами верхнего
левого угла и размерами;
Circle — окружность с заданными координатами центра и радиусом;
Ellipse — эллипс с заданными координатами верхнего угла описанного
вокруг него прямоугольника со сторонами, параллельными осям координат, и
размерами этого прямоугольника.
Создайте список фигур. Напишите функцию, которая сохраняет
каждую фигуру в отдельный файл, загружает фигуру из файла и отображает
информацию о каждой из фигур, включая площадь и периметр."""

from abc import ABC, abstractmethod
from math import pi, sqrt


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
    def load(self, path):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, name: str, unit_of_measurement: str, point_of_reference: list, side: int):
        self.__name = name
        self.__unit_of_measurement = unit_of_measurement
        self.__point_of_reference = point_of_reference
        self.__side = side

    def __str__(self):
        return (f'Название фигуры: {self.__name}\n'
                f'Единицы измерения: {self.__unit_of_measurement}\n'
                f'Координаты левого верхнего угла: {self.__point_of_reference}\n'
                f'Длина стороны: {self.__side} {self.__unit_of_measurement}')

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

    @property
    def point_of_reference(self):
        return self.__point_of_reference

    @point_of_reference.setter
    def point_of_reference(self, point_of_reference):
        self.__point_of_reference = point_of_reference

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.__side = side

    def area(self):
        return f'{self.side ** 2} Кв.{self.__unit_of_measurement}'

    def perimeter(self):
        return f'{self.side * 4} {self.__unit_of_measurement}'

    def save(self):
        lst = [('Фигура', square1.__name), ('Единицы измерения', square1.__unit_of_measurement),
               ('Координаты левого верхнего угла', square1.__point_of_reference), ('Длина стороны', square1.__side),
               ('Площадь фигуры', square1.area()), ('Периметр', square1.perimeter())]
        doc1 = ''
        file = 'square.txt'
        for i in lst:
            doc1 += str(i[0] + ':' + '\t' + str(i[1])) + '\n'
        square = open(file, 'w', encoding='utf-8')
        square.write(str(doc1))
        square.close()
        return file

    @classmethod
    def load(cls, path: str) -> object:
        #path = input('Введите название файла для загрузки квадрата: ')
        path = 'square'
        with open(path, 'r', encoding='utf-8') as file:
            figure = list(map(lambda x: x.rstrip('\n'), file.readlines()))
            figure[3] = int(figure[3])
        return cls(*figure)


square1 = Square('Квадрат', 'М', [2, 2], 5)

class Rectangle(Shape):
    def __init__(self, name: str, unit_of_measurement: str, point_of_reference: list, side_a: int, side_b: int):
        self.__name = name
        self.__unit_of_measurement = unit_of_measurement
        self.__point_of_reference = point_of_reference
        self.__side_a = side_a
        self.__side_b = side_b

    def __str__(self):
        return (f'Название фигуры: {self.__name}\n'
                f'Единицы измерения: {self.__unit_of_measurement}\n'
                f'Координаты левого верхнего угла: {self.__point_of_reference}\n'
                f'Длина стороны A: {self.__side_a} {self.__unit_of_measurement}\n'
                f'Длина стороны B: {self.__side_b} {self.__unit_of_measurement}')

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

    @property
    def point_of_reference(self):
        return self.__point_of_reference

    @point_of_reference.setter
    def point_of_reference(self, point_of_reference):
        self.__point_of_reference = point_of_reference

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, side_a):
        self.__side_a = side_a

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, side_b):
        self.__side_b = side_b

    def area(self):
        return f'{self.__side_a * self.__side_b} Кв. {self.__unit_of_measurement}'

    def perimeter(self):
        return f'{(self.__side_a + self.__side_b) * 2} {self.__unit_of_measurement}'

    def save(self):
        lst = [('Фигура', rectangle1.__name), ('Единицы измерения', rectangle1.__unit_of_measurement),
               ('Координаты левого верхнего угла', rectangle1.__point_of_reference), ('Длина стороны A',
                rectangle1.__side_a), ('Длина стороны B', rectangle1.__side_b), ('Площадь фигуры', rectangle1.area()),
               ('Периметр', rectangle1.perimeter())]
        doc1 = ''
        file = 'rect.txt'
        for i in lst:
            doc1 += str(i[0] + ':' + '\t' + str(i[1])) + '\n'
        rect = open(file, 'w', encoding='utf-8')
        rect.write(str(doc1))
        rect.close()
        return file

    @classmethod
    def load(cls, path: str) -> object:
        path = 'rectangle'
        with open(path, 'r', encoding='utf-8') as file:
            figure = list(map(lambda x: x.rstrip('\n'), file.readlines()))
            figure[3] = int(figure[3])
            figure[4] = int(figure[4])
        return cls(*figure)


rectangle1 = Rectangle('Прямоугольник', 'мм', [4, 4], 8, 12)


class Circle(Shape):
    def __init__(self, name: str, unit_of_measurement: str, point_of_reference: list, radius: int):
        self.__name = name
        self.__unit_of_measurement = unit_of_measurement
        self.__point_of_reference = point_of_reference
        self.__radius = radius

    def __str__(self):
        return (f'Название фигуры: {self.__name}\n'
                f'Единицы измерения: {self.__unit_of_measurement}\n'
                f'Координаты центра окружности: {self.__point_of_reference}\n'
                f'Радиус: {self.__radius} {self.__unit_of_measurement}')

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

    @property
    def point_of_reference(self):
        return self.__point_of_reference

    @point_of_reference.setter
    def point_of_reference(self, point_of_reference):
        self.__point_of_reference = point_of_reference

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def area(self):
        return f'{round(self.__radius ** 2 * pi), 2} {self.__unit_of_measurement}'

    def perimeter(self):
        return f'{round(2 * pi * self.__radius), 2} {self.__unit_of_measurement}'

    def save(self):
        lst = [('Фигура', round1.__name), ('Единицы измерения', round1.__unit_of_measurement),
               ('Координаты левого верхнего угла', round1.__point_of_reference), ('Радиус', round1.__radius),
               ('Площадь фигуры', round1.area()), ('Периметр', round1.perimeter())]
        doc1 = ''
        file = 'round.txt'
        for i in lst:
            doc1 += str(i[0] + ':' + '\t' + str(i[1])) + '\n'
        round = open(file, 'w', encoding='utf-8')
        round.write(str(doc1))
        round.close()
        return file

    @classmethod
    def load(cls, path: str) -> object:
        path = 'round'
        with open(path, 'r', encoding='utf-8') as file:
            figure = list(map(lambda x: x.rstrip('\n'), file.readlines()))
            figure[3] = float(figure[3])
        return cls(*figure)


round1 = Circle('Окружность', 'См', [6, 6], 4)

class Ellipse(Shape):
    def __init__(self, name: str, unit_of_measurement: str, point_of_reference: list, r1: int, r2: int):
        self.__name = name
        self.__unit_of_measurement = unit_of_measurement
        self.__point_of_reference = point_of_reference
        self.__r1 = r1
        self.__r2 = r2

    def __str__(self):
        return (f'Название фигуры: {self.__name}\n'
                f'Единицы измерения: {self.__unit_of_measurement}\n'
                f'Координаты левого верхнего угла описанного прямоугольника: {self.__point_of_reference}\n'
                f'Первый радиус: {self.__r1} {self.__unit_of_measurement}\n'
                f'Второй радиус: {self.__r2} {self.__unit_of_measurement}')

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

    @property
    def point_of_reference(self):
        return self.__point_of_reference

    @point_of_reference.setter
    def point_of_reference(self, point_of_reference):
        self.__point_of_reference = point_of_reference

    @property
    def r1(self):
        return self.__r1

    @r1.setter
    def r1(self, r1):
        self.__r1 = r1

    @property
    def r2(self):
        return self.__r2

    @r2.setter
    def r2(self, r2):
        self.__r2 = r2

    def area(self):
        return f'{round(int(self.__r1) * int(self.__r2) * pi),2} Кв. {self.__unit_of_measurement}'

    def perimeter(self) -> float:
        return f'{round(2 * pi * sqrt(((int(self.__r1)**2) + (int(self.__r2)**2)/2))), 2}{self.__unit_of_measurement}'

    def save(self):
        lst = [('Фигура', ellipse1.__name), ('Единицы измерения', ellipse1.__unit_of_measurement),
               ('Координаты левого верхнего угла описанного прямоугольника', ellipse1.__point_of_reference),
               ('Первый радиус', ellipse1.__r1), ('Второй радиус', ellipse1.__r2),
            ('Площадь фигуры', ellipse1.area()), ('Периметр', ellipse1.perimeter())]
        doc1 = ''
        file = 'ellipse.txt'
        for i in lst:
            doc1 += str(i[0] + ':' + '\t' + str(i[1])) + '\n'
        rect = open(file, 'w', encoding='utf-8')
        rect.write(str(doc1))
        rect.close()
        return file

    @classmethod
    def load(cls, path: str) -> object:
        path = 'ellipse'
        with open(path, 'r', encoding='utf-8') as file:
            figure = list(map(lambda x: x.rstrip('\n'), file.readlines()))
        return cls(*figure)


ellipse1 = Ellipse('Эллипс', 'Дм', [23, 34], 24, 36)

figures = [square1, rectangle1, round1, ellipse1]

def manipulation(figures: Shape):
    for i in figures:
        print(f'{i}\n'
              f'Площадь фигуры: {i.area()}\n'
              f'Периметр фигуры: {i.perimeter()}\n'
              f'Данные фигуры записаны в файл {i.save()}\n\n'
              f'Фигура загружена из файла.\n{i.load(str)}\n'
              f'Площадь равна: {i.load(str).area()}\n'
              f'Периметр равен: {i.load(str).perimeter()}\n')

def main():
    try:
        manipulation(figures)
    except ValueError as e:
        print(e)
    else:
        print('Программа завершена')

if __name__ == '__main__':
    main()

