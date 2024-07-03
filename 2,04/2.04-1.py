from abc import ABC

"""Задание 1.
Рассмотрим принцип единственной ответственности на следующем
примере. Допустим у нас есть класс RentCarService и в нем есть несколько
методов: найти машину по номеру, забронировать машину по номеру для
клиента, распечатать заказ на бронирование, получить информацию о
машине, отправить сообщение клиенту с информацией о его брони."""
"""Задание 2
Рассмотрим принцип открытости-закрытости на примере, созданного в
задании 1 класса по отправке сообщений NotificationService. Допустим нам
необходимо кроме отправки сообщения клиенту по электронной почте
отправлять еще смс сообщения. И мы можем дописать метод send_message
таким образом:
def send_message(type_message: str, message: str, client: Client)
if (type_message == "email"):
# send email
elif (type_message == "sms")
# send sms
Для того чтобы придерживаться принципа открытости-закрытости нам
необходимо спроектировать наш код таким образом, чтобы каждый мог
повторно использовать нашу функцию, просто расширив ее. Поэтому
определим абстрактный класс NotificationService и в нем поместим метод
send_message. Далее создайте класс EmailNotification, который наследуется
от NotificationService и реализует метод отправки сообщений по электронной
почте. Создайте аналогично класс MobileNotification, который будет отвечать
за отправку смс сообщений. Продемонстрируйте работу данного сервиса."""


class Car:
    def __init__(self, car_number: str):
        self._car_number = car_number

    def __str__(self):
        return f'Номер авто {self._car_number}'

    @property
    def car_number(self):
        return self._car_number

car1 = Car('A999RUS')
car2 = Car('A888RUS')
car3 = Car('A777RUS')
car4 = Car('A666RUS')
car5 = Car('A555RUS')

cars = [car1, car2, car3, car4, car5]

class Client:
    def __init__(self, name: str, telephone: int):
        self._name = name
        self._telephone = telephone

    def __str__(self):
        return (f'Клиент: {self._name}\n'
                f'Телефон: {self._telephone}')

    @property
    def get_name(self):
        return self._name

    @property
    def get_telephone(self):
        return self._telephone


client1 = Client('Иван', 23456)
client2 = Client('Василий', 454575)


class Order:
    def __init__(self, client: Client, car: Car):
        self._client = client
        self._car = car

    def __str__(self):
        return f'{self._client}, {self._car}'


class RentCarService:
    def __init__(self):
        self.__cars: list[Car] = []

    @property
    def get_cars(self):
        return self.__cars

    @staticmethod
    def search_car():
        if len(RentCarService.get_cars) == 0:
            return False
        else:
            return True

    @staticmethod
    def reservation_car(cars: list, client: Client):
        if not RentCarService.get_cars:
            print('Нет свободных авто!, попробуйте через 5 мин')
        else:
            order = Order(client, cars[0])
            print('Авто зарезервировано')
            return order



class CarPrintService:
    @staticmethod
    def print_order(order: Order):
        print(order)


class CarInfoService:
    @staticmethod
    def car_info(car: Car):
        return Car.car_number


class NotificationService(ABC):
    @staticmethod
    def send_message(message: str, client: Client):
        ...


class EmailNotification(NotificationService):
    @staticmethod
    def send_message(message: str, client: Client):
        print(f' отправлено сообщение по E-MAIL'
              f': {message}')


class MobileNotification(NotificationService):
    @staticmethod
    def send_message(message: str, client: Client):
        print(f' отправлено сообщение по SMS'
              f': {message}')


def add_zakaz(client: Client, cars: list, type_message: str):
    result = RentCarService.reservation_car(cars, client)
    CarPrintService.print_order(result)
    if type_message == 'Email':
        EmailNotification.send_message('Заявка отправлена', client)
    else:
        MobileNotification.send_message('Заявка отправлена', client)

add_zakaz(client1, cars, 'SMS')
add_zakaz(client2, cars, 'Email')
