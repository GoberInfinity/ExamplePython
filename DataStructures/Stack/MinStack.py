# -*- coding: utf-8 -*-
class MinStack:
    def __init__(self):
        self.stack = []
    
    def add(self, new_elem):
        # min(top, new_elem)
        new_min = new_elem if not self.stack else min(new_elem, self.stack[-1][1]) 
        self.stack.append((new_elem, new_min))
        
    def get_min(self):
        return self.stack[-1][1]
    
    def pop(self):
        return self.stack.pop()[0]
        
stack = MinStack()
stack.add(10)
stack.add(11)
stack.add(12)
print(f"Min of Stack {stack.get_min()}")
print(f"Pop element {stack.pop()}")
stack.add(1)
print(f"Min of Stack {stack.get_min()}")
print(f"Pop element {stack.pop()}")
print(f"Min of Stack {stack.get_min()}")