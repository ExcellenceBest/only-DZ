"""Задание 1
Фабричный метод позволяет разделить процесс создания объекта от
кода, который зависит от интерфейса объекта. Например, приложению
требуется объект с определенным интерфейсом. Это может объект у которого
конкретная реализация интерфейса зависит от некоторого параметра. Вместо
того чтобы использовать сложную условную структуру if-elif-else для
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

    def get_info(self):
        print('PDF')


class XMLDocument(Document):

    def get_info(self):
        print('XML')


class CreateDoc(ABC):

    @abstractmethod
    def create_doc(self) -> Document:
        ...

class PDFApplication(CreateDoc):

    def create_doc(self) -> Document:
        return PDFDocument()


class XMLApplication(CreateDoc):


    def create_doc(self) -> Document:
        return XMLDocument()


fabric = PDFDocument()
fabric.get_info()
fabric2 = XMLApplication()
fabric2.create_doc()
