from collections import deque
w = 10
u_screen = 1000
a1 = None 
stack = deque()

class CellularAutomata:
    def __init__(self,width):
        self.cells = [1 if x == width//2 else 0 for x in range(width)]
        self.generation = 0

    def nextGeneration(self):
        next_generation = [0] *len(self.cells)
        for i in range(1,len(self.cells)-2):
            left_n = self.cells[i-1]
            current_n = self.cells[i]
            right_n = self.cells[i+1]
            next_generation[i] = self.apply_rules(str(left_n) + str(current_n) + str(right_n))
        self.cells = next_generation
        self.generation += 1   
         
    def apply_rules(self,s_cells):
        rules = [0,1,0,1,1,0,1,0]
        number = int(s_cells,2)
        return rules[int(number)]
    
def setup():
    global stack,a1
    size(u_screen*2,u_screen)
    background(255)
    a1 = CellularAutomata(u_screen*2/w)
    stack.append(a1.cells)
    

def draw():
    global stack,a1
    for generation in range(len(stack)):
        for i,cell in enumerate(stack[generation]):
            if stack[generation][i]:
                fill(255)
            else:
                fill(0)
            stroke(0)
            rect(i*w,generation*w,w,w)
        
    if(len(stack) == u_screen//w):
        stack.popleft()

    a1.nextGeneration()
    stack.append(a1.cells) 
    
        
    
    