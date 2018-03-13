import random 
import copy

def setup():
    global cols, rows, counter, grid, resolution 
    #size(1600,1000)
    size(500,500)
    resolution = 10
    #rows = 1600 / resolution
    #cols = 1000 / resolution 
    rows = 500 / resolution
    cols = 500 / resolution 
    grid = make2DArray(cols,rows)
    #frameRate(5)

def draw():
    global cols, rows, counter, grid, resolution
    background(0)
    next_state = copy.deepcopy(grid)
    for i in xrange(1,rows+1):
        for j in xrange(1,cols+1):
            
            x = (i-1) * resolution
            y = (j-1) * resolution
            if grid[i][j] == 1:
                fill(255)
                rect(x,y, resolution, resolution)

            current_cell = grid[i][j]
            live_neighbours = count_neighbours(grid,i,j)
            
            if current_cell == 1:
                #underpopulation & overpopulation
                if live_neighbours < 2 or live_neighbours > 3:
                    next_state[i][j] = 0
            else:
                #reproduction
                if live_neighbours == 3:
                    next_state[i][j] = 1
    grid = copy.deepcopy(next_state)
    saveFrame("output/gol_#####.png")

def make2DArray(cols,rows):  
    arr = [[] for _ in xrange(rows+2)]
    for i in xrange(rows+2):
        for j in xrange(cols+2):
            if i == 0 or i == (rows + 1):
                arr[i].append(0)
            elif j == 0 or j == (cols + 1):
                arr[i].append(0)
            else:
                arr[i].append(random.randint(0,1))
    return arr     
    #return [[  for i in xrange(cols)] for i in xrange(rows)]
    

def count_neighbours(grid,i,j):
    return grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j-1] + grid[i][j+1] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]