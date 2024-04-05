from abc import ABC

from typing import List

"""Задание 1.
Рассмотрим принцип единственной ответственности на следующем
примере. Допустим у нас есть класс RentCarService и в нем есть несколько
методов: найти машину по номеру, забронировать машину по номеру для
клиента, распечатать заказ на бронирование, получить информацию о
машине, отправить сообщение клиенту с информацией о его брони."""

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
cars2 = []

class Client:
    def __init__(self, name: str, telephone: str):
        self._name = name
        self._telephone = telephone

    def __str__(self):
        return (f'Клиент: {self._name}\n'
                f'Телефон: {self._telephone}')

    @property
    def name(self):
        return self._name

    @property
    def telephone(self):
        return self._telephone


client1 = Client('Иван', '123456')
client2 = Client('Василий', '454575')


class Order:
    @staticmethod
    def print_order(order):
        print(f'Заказ оформлен!\n печать заказа: {order}')

class RentCarService:
    def __init__(self, car: Car):
        self._cars = car

    @staticmethod
    def search_car(car: list):
        if len(car) == 0:
            return False
        else:
            print('Найден свободный автомобиль!')
            return True

    @staticmethod
    def reservation_car(cars: list, client: Client):
        if RentCarService.search_car:
            print('Нет свободных авто!, попробуйте через 3 мин')
            RentCarService.search_car(car)
        else:
            order = (client, cars)
            print('Авто зарезервировано')
            return order


class CarPrintService:
    @staticmethod
    def print_order(order: Order):
        print(order)


class CarInfoService:
    def car_info(self, car: Car):
        return self.car_info(car)


class NotificationService(ABC):
    def send_message(self, message: str, client: Client):
        ...


class EmailNotification(NotificationService):
    @staticmethod
    def send_mail(message: str, client: Client):
        print(f'Клиенту {client} отправлено сообщение по E-MAIL'
              f': {message}')


class MobileNotification(NotificationService):
    @staticmethod
    def send_sms(message: str, client: Client):
        print(f'Клиенту {client} отправлено сообщение по SMS'
              f': {message}')


def zakaz(client: Client, all_cars: list):
    find_car = RentCarService.search_car(all_cars)
    result = RentCarService.reservation_car(find_car, client)
    Order.print_order(result)
    EmailNotification.send_mail('Заявка отправлена', client)

#zakaz(client1, cars)

zakaz(client2, cars2)


"""Необходимо создать класс CarPrintService и вынести туда функционал
печати заказа (класс Order). Работу связанную с получением информации об
автомобиле перенести в класс CarInfoService. Метод по отправке сообщений
клиенту (класс Client) перенести в класс NotificationService. Метод поиска
автомобиля (класс Car) по номеру и бронирование автомобиля в класс
RentCarService."""


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
