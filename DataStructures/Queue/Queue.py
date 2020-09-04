# -*- coding: utf-8 -*-
"""
Note: This is not the best approach to use Queue, use them if you want to 
manipulate the method of a Queue.
"""


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(4)
q.enqueue("dog")
q.enqueue(True)
q.dequeue()
