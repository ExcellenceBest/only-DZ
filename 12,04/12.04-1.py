"""Задание 1.
 Создайте набор классов для эмуляции сценариев работы сервиса для
заказа пиццы в модуле pizzeria.py
Классы должны позволять выполнять следующие сценарии:
1. Отобразить меню пиццерии с рецептами и составом пиццы.
2. Оформить заказ (клиент может заказать более 1 пиццы)
3. Отправка клиенту уведомления о готовности заказа и сроках
доставки
4. Отобразить информацию о заказе с сохранением в файл.
5. Оплатить заказ. Оплата заказа может производиться, как переводом,
так и картой.
6. Необходимо иметь возможность посмотреть количество заказов и
полную выручку за день.
Классы приложения должны быть построены с учетом принципов SOLID"""
from abc import ABC, abstractmethod
class Pizza:

    def __init__(self):
        self.title = None
        self.tomato = None
        self.mushrooms = None
        self.sausage = None
        self.cheese = None

    def __str__(self):
        return f'{self.title}'

class Maker(ABC):

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def set_title(self, title):
        ...

    @abstractmethod
    def set_tomato(self, tomato):
        ...

    @abstractmethod
    def set_mushrooms(self, mushrooms):
        ...

    @abstractmethod
    def set_sausage(self, sausage):
        ...

    @abstractmethod
    def set_cheese(self, cheese):
        ...

    @abstractmethod
    def get_pizza(self):
        ...


class PizzaMaker(Maker):

    _pizza: Pizza()

    def create(self):
        self._pizza = Pizza()

    def set_title(self, title):
        self._pizza.title = title

    def set_tomato(self, tomato):
        self._pizza.tomato = tomato

    def set_mushrooms(self, mushrooms):
        self._pizza.mushrooms = mushrooms

    def set_sausage(self, sausage):
        self._pizza.sausage = sausage

    def set_cheese(self, cheese):
        self._pizza.cheese = cheese

    def get_pizza(self):
        return self._pizza


class Manufacturing:

    def __init__(self, maker: Maker):
        self.__maker = maker

    def make(self) -> Pizza:
        self.__maker.create()
        self.__maker.set_title('4 Сыра')
        self.__maker.set_tomato(None)
        return self.__maker.get_pizza()


pizza_maker = PizzaMaker()
manufacturing = Manufacturing(pizza_maker)
pizza = manufacturing.make()
pizza2 = manufacturing.make()
a = pizza2.mushrooms

print(pizza)
print(pizza2)

class Order:
    ...





class Menu:

    def get_sostav(self, pizza: Pizza):
        return
