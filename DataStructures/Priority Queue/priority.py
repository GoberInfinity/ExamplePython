from queue import PriorityQueue

pque = PriorityQueue()

pque.put((2, "code"))
pque.put((1, "eat"))
pque.put((3, "sleep"))
# >>> (1, 'eat'), (2, 'code'), (3, 'sleep')

