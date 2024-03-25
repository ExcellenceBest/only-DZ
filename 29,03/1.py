from datetime import date

class Clock:
    def __init__(self, hours: date, minutes: date, seconds: date):
        self.hours = hours #self.__validate_hours(hours)
        self.minutes = minutes #self.__validate_minutes(minutes)
        self.seconds = seconds #self.__validate_seconds(seconds)

    @staticmethod
    def __validate_hours(hours):
        if hours > 23 or hours < 0:
            raise ValueError('Параметр часы вне диапазона от 0 до 23')

    @staticmethod
    def __validate_minutes(minutes):
        if minutes > 23 or minutes < 0:
            raise ValueError('Параметр минуты вне диапазона от 0 до 59')

    @staticmethod
    def __validate_seconds(seconds):
        if seconds > 23 or seconds < 0:
            raise ValueError('Параметр секунды вне диапазона от 0 до 59')

    def tick(self):
        if self.seconds == 59:
            if self.minutes == 59:
                if self.hours == 23:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
                    widget.advance()
                    print(widget)
                else:
                    self.hours += 1
                    self.minutes = 0
                    self.seconds = 0
                    print(widget)
            else:
                self.minutes += 1
                self.seconds = 0
                print(widget)
        else:
            self.seconds += 1
            print(widget)
class Calendar:
    def __init__(self, year: date, month: date, day: date):
        self.year = year #self.__validate_year(year)
        self.month = month #self.__validate_month(month)
        self.day = day #self.__validate_day(day)

    @staticmethod
    def __validate_year(year):
        if year > 2100 or year < 0:
            raise ValueError('Параметр год вне диапазона от 0 до 2100')

    @staticmethod
    def __validate_month(month):
        if month > 12 or month < 1:
            raise ValueError('Параметр месяц вне диапазона от 1 до 12')

    @staticmethod
    def __validate_day(day):
        if day > 31 or day < 1:
            raise ValueError('Параметр вне диапазона от 1 до 31')

    def advance(self):
        a = [1, 3, 5, 7, 8, 10, 12]
        if self.month :
            if self.day == 31:
                if self.month == 12:
                    self.year += 1
                    self.month = 1
                    self.day = 1
                else:
                    self.month += 1
            else:
                self.day = 1
                self.month += 1
        elif self.month == 2:
            if self.day == 28:
                self.month += 1
                self.day = 1
            else:
                self.day += 1
        else:
            if self.day == 30:
                self.month += 1
                self.day = 1
                self.day += 1
            else:
                self.day += 1

class CalendarClockWidget(Calendar, Clock):
    def __init__(self, year, month, day, hours, minutes, seconds):
        super().__init__(year, month, day)
        super().__init__(hours, minutes, seconds)
        self.year = year
        self.month = month
        self.day = day
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return (f'{self.year} {self.month} {self.day}\n'
                f'{self.hours} : {self.minutes} : {self.seconds}')

widget = CalendarClockWidget(2024, 5, 31, 23, 59, 57)
widget.tick()
widget.tick()
widget.tick()
widget.tick()
