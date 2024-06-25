"""
Опишите класс person, который имеет 3 атрибута, задающихся при инициализации.
Имя, возраст и память. Опишите следующие метода у данного класса, увеличение возраста на 1;
вывод имени, и текущего возраста; а так же переопределите методы сравнения для данного класса,
что бы людей можно было сравнивать между собой по возрасту. """


class Person:

    def __init__(self, name: str, age: int, memory: str):
        self._name = name
        self._age = age
        self._memory = memory

    def plus_year(self):
        self._age += 1
        return self._age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


    def __eq__(self, other):
        if isinstance(other, Person):
            return int(self._age) == other
        if isinstance(other, int):
            return int(self._age) == other


    def __ne__(self, other):
        if isinstance(other, Person):
            return self._age != other
        if isinstance(other, int):
            return self._age != other


    def __lt__(self, other):
        if isinstance(other, Person):
            return self._age < other
        if isinstance(other, int):
            return self._age < other


    def __ge__(self, other):
        if isinstance(other, Person):
            return self._age > other
        if isinstance(other, int):
            return self._age > other


person1 = Person('Вася', 10, 'Нормальная')
person2 = Person("Игорь", 12, "Плохая")
print(person2 == person1)
person1.plus_year()
person1.plus_year()
print(person1.get_age())
print(person2 == person1)
print(person2 != person1)
print(person2.get_name())
