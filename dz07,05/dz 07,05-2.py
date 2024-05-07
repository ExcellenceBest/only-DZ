"""Задание 1
Абстрактная фабрика является порождающим шаблоном
проектирования, который предоставляет интерфейс для создания семейств
взаимосвязанных или взаимозависимых объектов, не специфицируя их
конкретных классов. Этот шаблон реализуется созданием абстрактного класса
Factory, который представляет собой интерфейс для создания компонентов
системы.
Применим паттерн Абстрактная фабрика к построению некоего
производства автомобилей. Допустим, вы решили выйти на рынок
автомобилей и создать две собственные марки автомобиля. Для этого вам
нужна абстракция CarsFactory от которой будут наследоваться 2 конкретные
реализации фабрики под каждую марку автомобиля. На этих фабриках будут
делать автомобили с 2 типами кузова – седан и купе, поэтому каждая фабрика
должна уметь создавать автомобили, как седан, так и купе.
Таким образом, абстракция CarsFactory будет содержать 2 метода:
create_sedan и create_coupe. Соответственно, в дочерних классах интерфейса
CarsFactory, данные методы тоже должны быть реализованы.
Обратите внимание, что типом возвращаемого значения в методах
будет являться именно общий для возвращаемых значений тип – sedan и coupe.
Как несложно догадаться в программе должны появится некие абстракции,
описывающие конкретные типы кузова – седан и купе. Ну и конечно же,
данные абстракции должны иметь конкретную реализацию в виде
автомобилей, создаваемых на той или иной фабрике.
Вот и всё, наша «фабрика фабрик» способная производить автомобили
любой марки и любого типа, готова. В будущем вы можете решить, что было
бы неплохо начать выпускать внедорожники. Вам нужно будет создать ещё
одну абстракцию.
Продемонстрируйте работу данного паттерна и создайте по одному
экземпляру sedan и coupe любой марки автомобиля.
Родственные паттерны
Классы AbstractFactory часто реализуются фабричными методами, но
могут быть реализованы и с помощью паттерна прототип.
Конкретная фабрика часто описывается паттерном одиночка,
поскольку обычно нет нужды оставлять возможность создания нескольких
экземпляров одной и той же фабрики и в то же время создание отдельного
экземпляра может быть реализовано за счет паттерна строитель."""

from abc import ABC, abstractmethod

class Body(ABC):

    @abstractmethod
    def get_body(self):
        ...

class Sedan(Body):

    def get_body(self):
        print('Изготовлен Седан')

class Coup(Body):

    def get_body(self):
        print('Изготовлен Купе')

class CarFactory(ABC):

    @abstractmethod
    def create_sedan(self) -> Sedan:
        ...

    @abstractmethod
    def create_coup(self) -> Coup:
        ...


class Hyundai(CarFactory):

    def create_sedan(self) -> Sedan:
        print('Произведен Hyundai, модель седан')
        return Sedan()


    def create_coup(self) -> Coup:
        print('Произведен Hyundai, модель купе')
        return Coup()


class Mitsubishi(CarFactory):

    def create_sedan(self) -> Sedan:
        print('Произведен Mitsubishi, модель седан')
        return Sedan()

    def create_coup(self) -> Coup:
        print('Произведен Mitsubishi, модель купе')
        return Coup()


class Salon:

    def __init__(self, car_factory: CarFactory):
        self.__car_factory = car_factory


    def create_sedan(self):
        sedan = self.__car_factory.create_sedan()
        return sedan

    def create_coup(self):
        return self.__car_factory.create_coup()




mitsubishi = Mitsubishi()
salon = Salon(mitsubishi)
salon.create_sedan()
salon.create_coup()
hyundai = Hyundai()
salon1 = Salon(hyundai)
salon1.create_sedan()
salon1.create_coup()

# car1 = Mitsubishi.create_sedan(Mitsubishi)
# car2 = Hyundai.create_coup(Hyundai)
# car3 = Mitsubishi()
# car3.create_coup()
# car2.get_body()
