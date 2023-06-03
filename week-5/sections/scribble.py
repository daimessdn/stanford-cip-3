from graphics import Canvas
import time

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
DELAY = 0.01
CIRCLE_SIZE = 20

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # your animation code here :)
    
    circle_color = choose_color()
    
    while True:
        # get the coordinates of the mouse
        mouse_x, mouse_y = get_cursor_position(canvas)
        
        if get_boundary(mouse_x, mouse_y):
            create_circle(canvas, mouse_x, mouse_y, circle_color)
        
        time.sleep(DELAY)
        
def choose_color():
    """
    Get user color according to user input
    """
    
    valid_colors = ["red", "cyan", "yellow", "salmon", "green", "blue", "purple"]
    color = str(input(
        "Pick a color (%s): " % (", ".join(valid_colors))
    )).lower()
    
    while (color not in valid_colors):
        print("Color selected is invalid!")
        color = str(input(
            "Pick a color (%s): " % (", ".join(valid_colors))
        )).lower()
        
    print("Time to paint!")
    return color
    
def create_circle(canvas, x, y, color):
    """
    Creating circle according to the position
    """
    
    x_after, y_after = x + CIRCLE_SIZE, y + CIRCLE_SIZE
    
    canvas.create_oval(x, y, x_after, y_after, color)
    
def get_boundary(x, y):
    return x >= 0 and x <= CANVAS_WIDTH and y >+ 0 and y <+ CANVAS_HEIGHT
    
def get_cursor_position(canvas):
    """
    Getting a mouse coordinates according to cursor
    """
    
    return canvas.get_mouse_x(), canvas.get_mouse_y()

if __name__ == "__main__":
    main()