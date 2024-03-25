from datetime import datetime, date, time

class Clock:
    def __init__(self, hours: date, minutes: date, seconds: date):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        self.seconds = self.seconds + 1


class Calendar:
    def __init__(self, year: date, month: date, day: date):
        self.year = year
        self.month = month
        self.day = day

    def advance(self):
        ...


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

widget = CalendarClockWidget(2024, 3, 20, 15, 40, 30)
print(widget)
widget.tick()
print(widget)
widget.tick()
print(widget)

