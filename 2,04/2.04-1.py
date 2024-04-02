"""Задание 1.
Рассмотрим принцип единственной ответственности на следующем
примере. Допустим у нас есть класс RentCarService и в нем есть несколько
методов: найти машину по номеру, забронировать машину по номеру для
клиента, распечатать заказ на бронирование, получить информацию о
машине, отправить сообщение клиенту с информацией о его брони."""

class Car:
    ...

class Client:
    ...

class Order:
    ...


class RentCarService:
    def __init__(self):
        self.__cars: list[Car] = []

    def search_car(self, car_number: str):
        ...

    def reservation_car(self, car_number: str, client: Client):
        ...


class CarPrintService:
    def print_order(self, order: Order):
        ...

class CarInfoService:
    def car_info(self, car: Car):
        ...

class NotificationService:
    def send_message(self, message: str, client: Client):
        ...



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
