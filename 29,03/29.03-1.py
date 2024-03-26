from datetime import date

class Clock:
    """Класс имитирует часы.
    Attributes:
        - hours: date - часы
        - minutes: date - минуты
        - seconds: date - секунды
    Methods:
        - _validate_hours - валидация часов
        - _validate_minutes - валидация минут
        - _validate_seconds - валидация секунд
        - tick - метод при вызове сдвигает время на одну секунду вперед. """

    def __init__(self, hours: date, minutes: date, seconds: date):
        self.hours = self._validate_hours(hours)
        self.minutes = self._validate_minutes(minutes)
        self.seconds = self._validate_seconds(seconds)

    @staticmethod
    def _validate_hours(hours):
        if hours > 23 or hours < 0:
            raise ValueError('Параметр часы вне диапазона от 0 до 23')
        return hours

    @staticmethod
    def _validate_minutes(minutes):
        if minutes > 59 or minutes < 0:
            raise ValueError('Параметр минуты вне диапазона от 0 до 59')
        return minutes

    @staticmethod
    def _validate_seconds(seconds):
        if seconds > 59 or seconds < 0:
            raise ValueError('Параметр секунды вне диапазона от 0 до 59')
        return seconds

    def tick(self):
        if self.seconds == 59:
            if self.minutes == 59:
                if self.hours == 23:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
                    CalendarClockWidget.advance(self)
                    print(f'{widget}\n')
                else:
                    self.hours += 1
                    self.minutes = 0
                    self.seconds = 0
                    print(f'{widget}\n')
            else:
                self.minutes += 1
                self.seconds = 0
                print(f'{widget}\n')
        else:
            self.seconds += 1
            print(f'{widget}\n')

class Calendar:
    """Класс имитирует календарь.
        Attributes:
            - year: date - год
            - month: date - месяц
            - day: date - день
        Methods:
            - _validate_year - валидация годов
            - _validate_month - валидация месяцев
            - _validate_day - валидация дней
            -  advance - метод при вызове сдвигает календарь на один день вперед."""
    def __init__(self, year: date, month: date, day: date):
        self.year = self._validate_year(year)
        self.month = self._validate_month(month)
        self.day = self._validate_day(day)

    @staticmethod
    def _validate_year(year):
        if year > 2100 or year < 0:
            raise ValueError('Параметр год вне диапазона от 0 до 2100')
        return year

    @staticmethod
    def _validate_month(month):
        if month > 12 or month < 1:
            raise ValueError('Параметр месяц вне диапазона от 1 до 12')
        return month


    def _validate_day(self, day):
        if self.month == 2:
            if day > 28 or day < 1:
                raise ValueError('Параметр вне диапазона от 1 до 28')
        a = [1, 3, 5, 7, 8, 10, 12]
        if self.month in a:
            if day > 31 or day < 1:
                raise ValueError('Параметр  день вне диапазона от 1 до 31')
        else:
            if day > 30 or day < 1:
                raise ValueError('Параметр  день вне диапазона от 1 до 30')
        return day

    def advance(self):
        a = [1, 3, 5, 7, 8, 10, 12]
        if self.month in a:
            if self.day == 31:
                if self.month == 12:
                    self.year += 1
                    self.month = 1
                    self.day = 1
                else:
                    self.month += 1
                    self.day = 1
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

class CalendarClockWidget(Clock, Calendar):

    def __init__(self, year, month, day, hours, minutes, seconds):
        super().__init__(hours, minutes, seconds)
        super(Clock, self).__init__(year, month, day)

    def __str__(self):
        return (f'{self.year}-{self.month}-{self.day}\n'
                f'{self.hours}:{self.minutes}:{self.seconds}')

widget = CalendarClockWidget(2024, 12, 31, 23, 59, 58)

def test(gadget):
    gadget.tick()
    gadget.tick()
    gadget.tick()
    gadget.tick()

test(widget)
