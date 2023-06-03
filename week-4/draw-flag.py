from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

HALF_HEIGHT = CANVAS_HEIGHT / 2

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO, your code here
    
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, HALF_HEIGHT, "red")
    canvas.create_rectangle(0, HALF_HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT, "white")

if __name__ == '__main__':
    main()