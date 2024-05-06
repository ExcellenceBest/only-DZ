"""Задание 1
Фабричный метод позволяет разделить процесс создания объекта от
кода, который зависит от интерфейса объекта. Например, приложению
требуется объект с определенным интерфейсом. Это может объект у которого
конкретная реализация интерфейса зависит от некоторого параметра. Вместо
того, чтобы использовать сложную условную структуру if-elif-else для
выбора конкретной реализации, приложение делегирует это решение
отдельному компоненту, который создает объект.
В качестве примера реализуйте некоторое выдуманное приложение,
которому необходимо создать объект текстового документа в нужном
формате. Для этого определите абстракцию документа (класс Document) с
методом, который отображает его содержимое. Реализуйте наследников
документа PDFDocument и XMLDocument. Далее создайте абстрактный класс
приложения с методом, который должен создавать документ. Реализуйте
наследников приложения PDFApplication и XMLApplication, которые
реализуют метод создания определенного типа документов.
Протестируйте описанные классы на примере создания документа
определенного типа и отображения его содержимого."""

from abc import ABC, abstractmethod

class Document(ABC):

    @abstractmethod
    def get_info(self):
        ...


class PDFDocument(Document):

    def __init__(self, info: str):
        self.info = info

    def get_info(self):
        return self.info


class XMLDocument(Document):

    def __init__(self, info: str):
        self.info = info

    def get_info(self):
        return self.info


class CreateDoc(ABC):

    @abstractmethod
    def create_doc(self):
        ...

class PDFApplication(CreateDoc):

    def __init__(self, title):
        self.title = title

    def create_doc(self):
        return f'Создан документ {self.title} в формате PDF'


class XMLApplication(CreateDoc):

    def __init__(self, title):
        self.title = title


    def create_doc(self):
        return f'Создан документ {self.title} в формате XML'


doc1 = XMLApplication('file')
doc2 = PDFApplication('file2')
print(doc1.create_doc())
print(doc2.create_doc())
