x = 0
y = 0

square = 400
factor = 20
color_factor = 40
r = 0
g = 0
b = 0

def setup():
    global x, y
    size(400,400)
    background(0)
    x = square//2
    y = square//2

def draw():
    global x, y, z
    stroke(generate_color())
    strokeWeight(5)
    point(x,y)
    movement = ceil(random(0,4))

    if movement == 1:
        if not ((x+2) > square): 
            x += factor
    elif movement == 2:
        if (y-2) >= 0:
            y -= factor
    elif movement == 3:
        if (x-2) >= 0:
            x -= factor
    else:
        if not ((y+2) > square):
            y += factor
            
def generate_color():
    global r, g, b
    
    if b > 256:
        if g > 256:
            if r > 256:
                r = 0
                g = 0
                b = 0
            else:
                r += color_factor
                b = 0
                g = 0
        else:
            g += color_factor
            b = 0
    else:
        b += color_factor
    return '#'+(str(hex((r*65536)+(g*256)+b)))[2:]

                
    
    