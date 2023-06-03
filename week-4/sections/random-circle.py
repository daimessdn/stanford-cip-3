from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
N_CIRCLES = random.randint(1, 20)

def main():
    print('Random Circles')
    print("There are", N_CIRCLES, "circles")
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    for i in range(N_CIRCLES):
        
        CIRCLE_SIZE = random.randint(20, 50)
        
        x, y = get_random_coordinates()
        # print("Current (x, y, size)", x, y, CIRCLE_SIZE)
        x_fixed, y_fixed = fix_coordinates(x, y, CIRCLE_SIZE)
        # print("Fixed (x, y, size) = ", x_fixed, y_fixed, CIRCLE_SIZE)
        x_after, y_after = get_coordinates_after(x_fixed, y_fixed, CIRCLE_SIZE)
        
        canvas.create_oval(x_fixed, y_fixed, x_after, y_after, random_color())
        
def get_random_coordinates():
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_WIDTH)
    
    return x, y
        
def get_coordinates_after(x, y, size):
    return  x + size, y + size
    
def fix_coordinates(x, y, size):
    """
    Function to fix the circle coodinates
    so that the circle doesn't overlap within the canvas frame
    """
    fixed_x = x
    fixed_y = y
    
    if (x + size >= CANVAS_WIDTH):
        fixed_x = x /2
        
    if (y + size >= CANVAS_HEIGHT):
        fixed_y = (y / 2)
        
    return fixed_x, fixed_y
    
    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()