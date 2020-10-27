from queue import PriorityQueue

q = PriorityQueue()

q.put((100, "a not agent task"))
q.put((5, "a highly agent task"))
q.put((10, "an important task"))

while not q.empty():
    print(q.get())
