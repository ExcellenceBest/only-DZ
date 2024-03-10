"""Задание 1.
Реализуйте класс «Человек».
Необходимо хранить в полях класса: ФИО, возраст, контактный
телефон. Реализуйте конструктор по умолчанию и метод для вывода данных.
Реализуйте доступ к отдельным полям класса через методы класса (геттеры
и сеттеры).
Реализуйте метод класса, который принимает в качестве параметров
ФИО, дату рождения (день, месяц, год), контактный телефон. Создайте
экземпляр класса используя альтернативный конструктор.
Реализуйте статический метод, который вычисляет возраст человека
относительно текущего дня по переданной дате рождения """
from datetime import date

class Human:
    """Класс "Человек" описывает человека. Класс имеет атрибуты такие как:
        - name - ФИО
        - date_of_born - Дата рождения
        - telephone - Номер телефона
        Так же класс имеет следующие методы:
        - свойства атрибутов (@property) для их вывода
        - сеттеры атрибутов (@атрибут.setter) для изменения значений атрибутов
        - create_human_alternative - класс-метод для создания объекта """

    def __init__(self, name: list, date_of_born: date, telephone: str):
        self.__name = name
        self.__date_of_born = date_of_born
        self.__telephone = telephone

    @classmethod
    def create_human_alternative(cls, path: str) -> object:
        """Метод позволяет создавать экземпляры класса альтернативным способом,
        принимает в себя параметр path: str(путь к файлу) и возвращает объект класса."""
        with open(path, 'r', encoding='utf-8') as file:
            create_human = list(map(lambda x: x.rstrip('\n'), file.readlines()))
            create_human[1] = create_human[1]
            create_human[2] = str(create_human[2])

        return cls(*create_human)

    def __str__(self):
        """Метод для вывода информации всех значений атрибутов на печать"""

        return (f'ФИО: {self.name} \n'
                f'Дата рождения: {self.__date_of_born}\n'
                f'Телефон: {self.__telephone}\n')

    @property
    def name(self) -> list:
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def date_of_born(self) -> date:
        return self.__date_of_born

    @date_of_born.setter
    def date_of_born(self, date_of_born):
        self.__date_of_born = date_of_born

    @property
    def telephone(self) -> str:
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        self.__telephone = telephone

    @staticmethod
    def lived_through():
        now = date.today()
        human_birthday = human1.__date_of_born
        age = now.year - human_birthday.year
        return age


human1 = Human(['Иванов', 'Иван', 'Иванович'], date(1984, 9, 4), '+7-964-136-5667')
print(human1)
print(human1.lived_through())
human2 = Human.create_human_alternative('Human.txt')
print(human2)
