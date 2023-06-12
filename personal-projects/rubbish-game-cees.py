from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
VELOCITY = 3
DELAY = 0.1

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # create bin 
    start_x = 10
    start_y = 250
    i = 0

    bin_can = canvas.create_rectangle(start_x, start_y, start_x + 100, start_y + 150, 'green', outline = 'black')
    lid = canvas.create_rectangle(0, 230, 120, 250, 'yellow', outline= 'black')
    recycle_text = canvas.create_text(25, 300, text = 'RECYCLE', font_size = 15)

    # create trash fall 
    trash_list = []
    for trash_index in range(100):
        trash_size = random.randint(20, 30)

        START_X = random.randint(110, CANVAS_WIDTH - trash_size)
        START_Y = 0

        trash = canvas.create_rectangle(START_X, START_Y, START_X + trash_size, START_Y + trash_size, 'brown')
        trash_list.append((trash, START_X, START_Y, trash_size))

        trash_in_text = canvas.create_text(300, 20, text = "Trash-in : " + str(i), font_size=15)
        
        trash_touched = False

        while True:
            for index, (trash, trash_x, trash_y, trash_size) in enumerate(trash_list):
                # move the trash down the screen
                ## if the trash is not clicked
                if not trash_touched:
                    START_Y += VELOCITY
                    canvas.moveto(trash, START_X, START_Y)
                else:
                    # in case the trash is clicked
                    ## move the trash to the mouse position
                    mouse_x = canvas.get_mouse_x()
                    mouse_y = canvas.get_mouse_y()

                    START_X = mouse_x
                    START_Y = mouse_y

                    canvas.moveto(trash, START_X, START_Y)

                # mechanism for opening the trash can
                ## bin lid open
                mouse_x = canvas.get_mouse_x()
                mouse_y = canvas.get_mouse_y()

                if mouse_x <= 130 and mouse_y >= 230:
                    canvas.moveto(lid, 0, 130)
                else:
                    canvas.moveto(lid, 0, 230)
                
                ## check if the mouse touches the trash
                x = canvas.get_mouse_x()
                y = canvas.get_mouse_y()
                
                # in case the mouse has touched the trash
                if (START_X - trash_size <= mouse_x <= START_X + trash_size) and (START_Y - trash_size <= mouse_y <= START_Y + trash_size):
                    # change the trash clicked status to True
                    ## so that the trash can be moved using mouse interaction
                    trash_touched = True

                # in case the trash is put into the bin
                if START_Y >= CANVAS_HEIGHT - trash_size or (START_X < 110 and START_Y > 230):
                    # reset trash condition and change the text
                    i+=1
                    trash_touched = False
                    canvas.change_text(trash_in_text, "Trash-in : " + str(i))

                    # reset the trash position to the top with a new random X-coordinate
                    START_Y = 0
                    START_X = random.randint(110, CANVAS_WIDTH - trash_size)
                    canvas.moveto(trash, START_X, START_Y)
                
            time.sleep(DELAY)
    
if __name__ == '__main__':
    main()