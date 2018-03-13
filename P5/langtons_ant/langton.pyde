matrix = [[]]
resolution = 0
square_cells = 0
current_cell = []
current_direction = ""

movements_rules = {'UP_LT':(-1,0),
                   'UP_RT':(1,0),
                   'RT_LT':(0,-1),
                   'RT_RT':(0,1),
                   'DW_LT':(1,0),
                   'DW_RT':(-1,0),
                   'LT_LT':(0,1),
                   'LT_RT':(0,-1),}

direction_states = ('UP','RIGHT','DOWN','LEFT')

def setup():
    global matrix, square_cells, current_cell, current_direction, resolution
    size(900,900)
    resolution = 5
    square_cells = 900 / resolution 
    matrix = make_matrix(square_cells)
    current_cell = [100,100]
    current_direction = direction_states[0]
    #frameRate(2)
    
def draw():
    global matrix, current_cell, current_direction, first_time
    background(255)
    for x_m in range(square_cells):
        for y_m in range(square_cells):
            x = x_m * resolution
            y = y_m * resolution
            if matrix[x_m][y_m] == 1:
                fill(0)
                rect(x,y, resolution, resolution)
                
    if current_cell[0] > square_cells or current_cell[1] > square_cells:
        pass
    else:
        if matrix[current_cell[0]][current_cell[1]] == 0:
            matrix[current_cell[0]][current_cell[1]] = 1    
            if current_direction == 'UP':
                rule = get_rule('UP_RT')
                current_direction = direction_states[1]
            elif current_direction == 'RIGHT':
                rule = get_rule('RT_RT')
                current_direction = direction_states[2]
            elif current_direction == 'DOWN':
                rule = get_rule('DW_RT')
                current_direction = direction_states[3]
            elif current_direction == 'LEFT':
                rule = get_rule('LT_RT')
                current_direction = direction_states[0]
            else:
                rule = [0,0]
        
        else:
            matrix[current_cell[0]][current_cell[1]] = 0
            if current_direction == 'UP':
                rule = get_rule('UP_LT')
                current_direction = direction_states[3]
            elif current_direction == 'RIGHT':
                rule = get_rule('RT_LT')
                current_direction = direction_states[0]
            elif current_direction == 'DOWN':
                rule = get_rule('DW_LT')
                current_direction = direction_states[1]
            elif current_direction == 'LEFT':
                rule = get_rule('LT_LT')
                current_direction = direction_states[2]
            else:
                rule = [0,0]
                
        current_cell[0] += rule[0]
        current_cell[1] += rule[1]        
            
def make_matrix(cells):
    return [[0] * (cells + 1) for _ in range(cells+1)]

def get_rule(rule):
    return movements_rules.get(rule)
    