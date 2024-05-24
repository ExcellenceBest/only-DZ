"""Задание 1
Создайте класс очереди для работы с объектами определенного типа.
Очередь должна иметь определенный размер.
Реализуйте набор операций для работы с очередью:
 Проверка очереди на пустоту;
 Добавление элемента в очередь;
 Удаление элемента из очереди;
 Очистить очередь;
 Получение значения из вершины из очереди.
Задание 2
Разработать приложение, имитирующее очередь печати принтера. На
принтер отправляются документы, которые печатаются в порядке очереди.
Память принтера ограничена. Необходимо сохранять статистику печати
документа (время начала печати, название документа) в отдельный файл.
Продемонстрируйте работу с печатью нескольких документов."""

class Queue:

    def __init__(self, len_max=3):
        self._data = []
        self._len_max = len_max

    def is_empty(self):
        return len(self._data) == 0

    def is_full(self):
        return len(self._data) == self._len_max

    def enqueue(self, item):
        if len(self._data) < self._len_max:
            self._data.append(item)
        else:
            return print("Очередь переполнена!")

    def dequeue(self):
        if len(self._data) == 0:
            raise ValueError("Очередь пуста!!!")
        else:
            return self._data.pop(0)

    def clear_queue(self):
        return self._data.clear()

    def peek(self):
        if len(self._data) == 0:
            return 'Очередь пуста!'
        else:
            return self._data[0]

queue = Queue()
class Printer(Queue):

    file = 'doc.txt'

    def __init__(self, queue: Queue):
        super().__init__()
        self._queue = queue

    def __str__(self):
        return f'Очередь: {self._data}'

    @staticmethod
    def save_doc(path: str):
        ...

docs = ["doc1.txt", "doc2.txt", "doc3.txt", "doc4.txt"]
docs1 = ['doc9']
xerox = Printer(queue=3)

def print_doc(docs: list):
    for i in docs:
        if xerox.is_full():
            print(xerox.is_full())
            x = xerox.dequeue()
            print(f'{x} напечатан')
            xerox.save_doc(x)
        else:
            xerox.enqueue(i)
            print(f'{i} отправлен на печать')
    while not xerox.is_empty():
        x = xerox.dequeue()
        print(f'{x} напечатан')


#print_doc(docs)

print(xerox)
print(xerox.peek())
xerox.enqueue("doc1.txt")
print(xerox.peek())
xerox.enqueue("doc2.txt")
xerox.enqueue('doc3.txt')
xerox.enqueue("doc4.txt")
print(xerox.peek())
print(xerox.is_empty())
print(xerox)
