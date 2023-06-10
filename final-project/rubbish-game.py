from graphics import Canvas
import random
import time
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

DELAY = 0.01

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    bin_position = { "x": 10, "y": 290 }
    bin = canvas.create_rectangle(
        bin_position["x"], bin_position["y"],
        bin_position["x"] + 70, bin_position["y"] + 100,
        "blue"
    )
    
    rubbish = None
    rubbish_position = { "x": None, "y": None }
    
    score = 0
    
    while True:
        # create the rubbish bin if not exist
        if rubbish == None:
            rubbish_x = random.randint(10, CANVAS_HEIGHT - 10)
            rubbish_y = 10
            rubbish_position = { "x": rubbish_x, "y": rubbish_y }
            
            rubbish = canvas.create_oval(
                rubbish_position["x"], rubbish_position["y"],
                rubbish_position["x"] + 10, rubbish_position["y"] + 10,
                "brown"
            )
        else:
            # move the rubbish toward bottom
            rubbish_y += 5
            rubbish_position = { "x": rubbish_x, "y": rubbish_y }
            
            canvas.moveto(rubbish, rubbish_position["x"], rubbish_position["y"])
            
        # mechanism for moving the rubbish bin
        x = canvas.get_mouse_x()
        
        if x >= 10 and x < CANVAS_WIDTH - 60:
            # print(x)
            bin_position = { "x": x, "y": 290 }
            canvas.moveto(bin, bin_position["x"], bin_position["y"])
            
        # check for rubbish bin overlap
        bin_overlap = canvas.find_overlapping(
            rubbish_position["x"], rubbish_position["y"],
            rubbish_position["x"] + 10, rubbish_position["y"] + 10
        )
        
        # print(bin_overlap)
        
        """
        check for the rubbish and bin overlap
        in this case, "shape_0" represents the rubbish
        """
        if "shape_0" in bin_overlap:
            canvas.delete(rubbish)
            
            score += 1
            print("rubbish collected, current score:", score)
            
            rubbish_x = random.randint(10, CANVAS_HEIGHT - 10)
            rubbish_y = 10
            rubbish_position = { "x": rubbish_x, "y": rubbish_y }
            
            rubbish = canvas.create_oval(
                rubbish_position["x"], rubbish_position["y"],
                rubbish_position["x"] + 10, rubbish_position["y"] + 10,
                "brown"
            )
        
        
        """
        in case, "shape_0" is in the bottom (y = 380)
        the rubbish is not collected
        """
        if rubbish_position["y"] > 380:
            canvas.delete(rubbish)
            
            rubbish_x = random.randint(10, CANVAS_HEIGHT - 10)
            rubbish_y = 10
            rubbish_position = { "x": rubbish_x, "y": rubbish_y }
            
            rubbish = canvas.create_oval(
                rubbish_position["x"], rubbish_position["y"],
                rubbish_position["x"] + 10, rubbish_position["y"] + 10,
                "brown"
            )
        
        time.sleep(DELAY)

if __name__ == '__main__':
    main()