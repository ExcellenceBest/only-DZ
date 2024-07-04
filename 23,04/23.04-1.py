"""Задание 1.
Создайте класс очереди для работы с объектами определенного типа.
Очередь должна иметь определенный размер.
Реализуйте набор операций для работы с очередью:
 Проверка очереди на пустоту;
 Добавление элемента в очередь;
 Удаление элемента из очереди;
 Очистить очередь;
 Получение значения из вершины из очереди.
Задание 2.
Разработать приложение, имитирующее очередь печати принтера. На
принтер отправляются документы, которые печатаются в порядке очереди.
Память принтера ограничена. Необходимо сохранять статистику печати
документа (время начала печати, название документа) в отдельный файл.
Продемонстрируйте работу с печатью нескольких документов."""
from datetime import datetime
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

    def __init__(self, queue: Queue):
        super().__init__()
        self._queue = queue

    @staticmethod
    def get_time():
        new_date = datetime.now()
        start_time = new_date.time()
        return start_time

    def __str__(self):
        return f'Очередь: {self._data}'

    @staticmethod
    def save_doc(file: str, start_time: str):
        with open('statistic.txt', 'a', encoding='utf-8') as stat:
            stat.write(f'Документ: {file},')
            stat.write(f' Время начала печати: {start_time}\n')


docs = ["doc1.txt", "doc2.txt", "doc3.txt", "doc4.txt", "doc5.txt", "doc6.txt", "doc7.txt"]
xerox = Printer(queue=3)

def print_doc(docs: list):
    for i in docs:
        if xerox.is_full():
            print('Очередь наполнена, идет печать')
            x = xerox.dequeue()
            print(f'{x} напечатан')
            xerox.enqueue(i)
            print(f'{i} отправлен на печать')
            xerox.save_doc(i, Printer.get_time())
        else:
            xerox.enqueue(i)
            print(f'{i} отправлен на печать')
            xerox.save_doc(i, Printer.get_time())
    while not xerox.is_empty():
        x = xerox.dequeue()
        print(f'{x} напечатан')


def main():
    try:
        print_doc(docs)
    except OSError as e:
            print(e)
    except TypeError as e:
        print(e)
    else:
        print('Работа функции завершена успешно!')
if __name__ == '__main__':
     main()

