from typing import List
from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data: List = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        deleted_value = self._data[0]
        del self._data[0]
        return deleted_value

    def search(self, index):
        list_length = len(self._data)
        if index in range(list_length):
            return self._data[index]
        else:
            raise IndexError('Índice Inválido ou Inexistente')
