# -*- coding: utf-8 -*-
import queue
# The constructor for a FIFO queue is as follows:
#  class Queue.Queue(maxsize=0)
q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())
