import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    file1 = {"qtd_linhas": 9}
    file2 = {"qtd_linhas": 4}
    file3 = {"qtd_linhas": 2}
    file4 = {"qtd_linhas": 5}
    file5 = {"qtd_linhas": 7}
    file6 = {"qtd_linhas": 11}
    file7 = {"qtd_linhas": 3}

    priority_queue.enqueue(file1)
    priority_queue.enqueue(file2)
    priority_queue.enqueue(file3)
    priority_queue.enqueue(file4)
    priority_queue.enqueue(file5)
    priority_queue.enqueue(file6)
    priority_queue.enqueue(file7)

    assert len(priority_queue) == 7
    with pytest.raises(IndexError):
        priority_queue.search(15)

    assert priority_queue.dequeue() == file2   
    assert priority_queue.search(0) == file3
    assert priority_queue.dequeue() == file3
    assert priority_queue.dequeue() == file7
    assert priority_queue.search(0) == file1