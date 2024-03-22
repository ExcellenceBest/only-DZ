class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        ...


class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def advance(self):
        ...


class CalendarClockWidget(Clock, Calendar):
    def __init__(self, year, month, day, hours, minutes, seconds):
        (super().__init__(hours, minutes, seconds),
         super().__init__(year, month, day))


    def __str__(self):
        return (f'{self.year}-{self.month}-{self.day}\n'
                f'{self.hours}:{self.minutes}:{self.seconds}')

widget = CalendarClockWidget(2024, 3, 20, 15, 4, 10)
print(widget)


