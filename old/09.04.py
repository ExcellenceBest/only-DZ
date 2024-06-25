"""
Создайте набор классов для эмуляции сценариев работы сервиса для
Написать программу «Автоматизированная информационная система ЖД
вокзала». Система содержит: сведения об отправлении поездов дальнего
следования. Для каждого поезда укажите: номер, время и дату отправления,
станцию отправления и назначения. Реализуйте:
 Вывод расписания о всех поездах за указанную дату;
 Вывод информации о запрашиваемом поезде."""
from datetime import date, time

class Train:


    def __init__(self, train_number: int, departure_data: date, departure_time: time,
                 departure_station: str, destination_station: str):
        self._train_number = train_number
        self._departure_data = departure_data
        self._departure_time = departure_time
        self._departure_station = departure_station
        self._destination_station = destination_station

    @property
    def get_train_number(self):
        return self._train_number

    @property
    def get_departure_data(self):
        return self._departure_data


    def __str__(self):
        return (f'Номер поезда: {self._train_number}, '
                f'Дата отправления: {self._departure_data}, '
                f'Время отправления: {self._departure_time}, '
                f'Станция отправления: {self._departure_station}, '
                f'Станция назначения: {self._destination_station}')


class Train_park:

    park: [Train] = []

    @staticmethod
    def add_train(train: [Train]):
        Train_park.park.append(train)

    @staticmethod
    def train_info(number: int):
        for i in Train_park.park:
            if number == i.get_train_number:
                return i
        print('поезда с таким номером нет в списке')

    @staticmethod
    def train_schedule(data: date):
        result = []
        for i in Train_park.park:
            if data == i.get_departure_data:
                result.append(i)
        return result

    @staticmethod
    def info(train: list):
        for i in train:
            print(i)


station = Train_park

first_train = Train(1, date(2024, 12, 29), time(12, 23, 45), 'Yaroslavl', "Moscow")
station.add_train(first_train)
train2 = Train(2, date(2024, 12, 29), time(12, 23, 45), 'Yaroslavl', "Kiev")
train3 = Train(3, date(2024, 12, 29), time(10, 23, 48), 'Kostroma', "Kiev")
train4 = Train(4, date(2024, 12, 28), time(00, 00, 45), 'Yaroslavl', "Piter")
train5 = Train(5, date(2024, 12, 28), time(12, 40, 45), 'Yaroslavl', "Kiev")
station.add_train(train2)
station.add_train(train3)
station.add_train(train4)
station.add_train(train5)
print(Train_park.train_info(1))
q = station.train_schedule(date(2024, 12, 28))
station.info(q)
