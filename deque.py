class Queue:

    def __init__(self, len_max):
        self._data = []
        self._len_max = len_max

    def is_empty(self):
        return len(self._data) == 0

    def is_full(self):
        return len(self._data) == self._len_max


    def enqueue(self, item):
        if len(self._data) < self._len_max:
            self._data.append(item)

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


class Printer(Queue):

    def __init__(self, len_max):
        Queue.__init__(self, 2)
        self._len_max = len_max



    def __str__(self):
        return f'Очередь: {self._data}'

    @staticmethod
    def save_doc(path: str):
        ...

docs = ["doc1.txt", "doc2.txt", "doc3.txt", "doc4.txt", "doc5.txt"]
docs1 = ['doc9']
xerox = Printer(3)

def print_doc(document: list):
    for i in document:
        if xerox.is_full():
            print("Очередь переполнена!")
            x = xerox.dequeue()
            print(f'{x} напечатан')
            xerox.enqueue(i)
            print(f'{i} отправлен на печать')
            xerox.save_doc(x)
        else:
            xerox.enqueue(i)
            print(f'{i} отправлен на печать')
    while not xerox.is_empty():
        x = xerox.dequeue()
        print(f'{x} напечатан')


print_doc(docs)

# print(xerox)
# print(xerox.peek())
# xerox.enqueue("doc1.txt")
# print(xerox.peek())
# xerox.enqueue("doc2.txt")
# xerox.enqueue('doc3.txt')
# xerox.enqueue("doc4.txt")
# print(xerox.peek())
# print(xerox.is_empty())
# print(xerox)
