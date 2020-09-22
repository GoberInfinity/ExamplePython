class MinQueue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def add(self, new_elem):
        # min(top, new_elem)
        # Add new elements to the stack s1, and remove elements from the stack s2
        new_min = new_elem if not self.stack_1 else min(new_elem, self.stack_1[-1][1])
        self.stack_1.append((new_elem, new_min))

    def get_min(self):
        if not self.stack_1 or not self.stack_2:
            return self.stack_1[-1][1] if not self.stack_2 else self.stack_2[-1][1]
        return min(self.stack_1[-1][1], self.stack_2[-1][1])

    def pop(self):
        if not self.stack_2:
            while self.stack_1:
                elem = self.stack_1.pop()[0]
                minimum = elem if not self.stack_2 else min(elem, self.stack_2[-1][1])
                self.stack_2.append((elem, minimum))
        return self.stack_2.pop()[0]


que = MinQueue()
que.add(1)
que.add(2)
que.add(3)
print(f"Min of MinQueue {que.get_min()}")
que.add(4)
que.add(5)
print(f"Min of MinQueue {que.get_min()}")
print(f"Pop element {que.pop()}")
print(f"Min of MinQueue {que.get_min()}")
print(f"Pop element {que.pop()}")
print(f"Min of MinQueue {que.get_min()}")
que.add(6)
print(f"Min of MinQueue {que.get_min()}")
