from graphics import Canvas

# added canvas size constant
CANVAS_SIZE = 400

def main():
    # draws two cars
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE) # update by canvas size constant
    x = 10
    y = 10
    draw_car(canvas, x, y) # added argument canvas, x, y in this line

    x = 100
    y = 100
    draw_car(canvas, x, y) # added argument canvas, x, y in this line

def draw_car(canvas, x, y): # added argument canvas, x, y in this line
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    
    # validating the car offset
    if (x + 60 <= CANVAS_SIZE and y + 50 <= CANVAS_SIZE):
        canvas.create_rectangle(x + 10, y + 10, x + 60, y + 30) # added every arguments by 10
        canvas.create_rectangle(x + 20, y, x + 50, y + 30)      # added every arguments by 10

if __name__ == '__main__':
    main()
