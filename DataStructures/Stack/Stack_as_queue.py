# -*- coding: utf-8 -*-
import queue

q = queue.LifoQueue()

# add items at the head of the queue
for x in range(4):
    q.put("item-" + str(x))

# remove items from the head of the queue
while not q.empty():
    print(q.get())
