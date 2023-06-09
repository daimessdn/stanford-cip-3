"""
GOBAK SODOR

Gobak Sodor is a group-based game which has two groups: the defenders and the escapers.
The group of defender's role is to make sure the escaper's group are being get caught and
not reach the finish line, while the group od escaper's role is to make sure they don't
being caught by the defenders group and reach the finish line.

In this game, assuming we play as a single escaper (one character with pale orange color face).
The instruction is simple, reaching the finish line (black line on the top) without getting caught
by the enemy (defender's group, character with reddish face).

Check it out:

https://codeinplace.stanford.edu/cip3/share/Ls1HGeDb7OFdF1KmuDI9

https://codeinplace.stanford.edu/cip3/share/Ls1HGeDb7OFdF1KmuDI9

https://codeinplace.stanford.edu/cip3/share/Ls1HGeDb7OFdF1KmuDI9
"""

from graphics import Canvas
import time
import math
import random

DELAY_INTERVAL = .05
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 800

PLAYER_X = 160
PLAYER_Y = CANVAS_HEIGHT - 90

ENEMY1_X = random.randint(10, CANVAS_WIDTH - 90)
ENEMY1_Y = 460

ENEMY2_X = random.randint(10, CANVAS_WIDTH - 90)
ENEMY2_Y = 180

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "#52b788")
    
    # draw decoration
    draw_grass(canvas, 150, 120)
    draw_grass(canvas, 220, 300)
    draw_grass(canvas, 130, 430)
    draw_grass(canvas, 300, 560)
    draw_grass(canvas, 50, 640)
    
    # victory area instance
    victory_area = canvas.create_rectangle(10, 10, CANVAS_WIDTH - 10, 25, "#222")
    
    coords = { "x": PLAYER_X, "y": PLAYER_Y }
    enemy1_coords = { "x": ENEMY1_X, "y": ENEMY1_Y, "movement": (-10 if random.random() > 0.5 else 10) }
    enemy2_coords = { "x": ENEMY2_X, "y": ENEMY2_Y, "movement": (-10 if random.random() > 0.5 else 10) }
   
    # player instances
    player = {
        "face": canvas.create_oval(coords["x"], coords["y"], coords["x"] + 80, coords["y"] + 80, "#fad9b6"),
        "left_eye": canvas.create_oval(coords["x"] + 20, coords["y"] + 20, coords["x"] + 30, coords["y"] + 30, "#222"),
        "right_eye": canvas.create_oval(coords["x"] + 50, coords["y"] + 20, coords["x"] + 60, coords["y"] + 30, "#222"),
        "nose": canvas.create_polygon(coords["x"] + 30, coords["y"] + 50, coords["x"] + 50, coords["y"] + 50,  coords["x"] + 40, coords["y"] + 20, color="#222"),
        "mouth": canvas.create_polygon(coords["x"] + 30, coords["y"] + 60, coords["x"] + 50, coords["y"] + 60,  coords["x"] + 40, coords["y"] + 70, color="#222"),
    }
    
    # enemies instances
    enemy1 = {
        "face": canvas.create_oval(enemy1_coords["x"], enemy1_coords["y"], enemy1_coords["x"] + 80, enemy1_coords["y"] + 80, "#f27059"),
        "left_eye": canvas.create_oval(enemy1_coords["x"] + 20, enemy1_coords["y"] + 20, enemy1_coords["x"] + 30, enemy1_coords["y"] + 30, "#222"),
        "right_eye": canvas.create_oval(enemy1_coords["x"] + 50, enemy1_coords["y"] + 20, enemy1_coords["x"] + 60, enemy1_coords["y"] + 30, "#222"),
        "nose": canvas.create_polygon(enemy1_coords["x"] + 30, enemy1_coords["y"] + 50, enemy1_coords["x"] + 50, enemy1_coords["y"] + 50,  enemy1_coords["x"] + 40, enemy1_coords["y"] + 20, color="#222"),
        "mouth": canvas.create_polygon(enemy1_coords["x"] + 30, enemy1_coords["y"] + 60, enemy1_coords["x"] + 50, enemy1_coords["y"] + 60,  enemy1_coords["x"] + 40, enemy1_coords["y"] + 70, color="#222"),
    }
    enemy2 = {
        "face": canvas.create_oval(enemy2_coords["x"], enemy2_coords["y"], enemy2_coords["x"] + 80, enemy2_coords["y"] + 80, "#f27059"),
        "left_eye": canvas.create_oval(enemy2_coords["x"] + 20, enemy2_coords["y"] + 20, enemy2_coords["x"] + 30, enemy2_coords["y"] + 30, "#222"),
        "right_eye": canvas.create_oval(enemy2_coords["x"] + 50, enemy2_coords["y"] + 20, enemy2_coords["x"] + 60, enemy2_coords["y"] + 30, "#222"),
        "nose": canvas.create_polygon(enemy2_coords["x"] + 30, enemy2_coords["y"] + 50, enemy2_coords["x"] + 50, enemy2_coords["y"] + 50,  enemy2_coords["x"] + 40, enemy2_coords["y"] + 20, color="#222"),
        "mouth": canvas.create_polygon(enemy2_coords["x"] + 30, enemy2_coords["y"] + 60, enemy2_coords["x"] + 50, enemy2_coords["y"] + 60,  enemy2_coords["x"] + 40, enemy2_coords["y"] + 70, color="#222"),
    }
     
    # text and time instance
    corner_text = canvas.create_text(120, 10, font="Helvetica", text="GOBAK SODOR GAME", font_size=16, color="#fff")
    corner_text_2 = canvas.create_text(10, 32, font="Helvetica", text="Escape from the enemies and don't get caught", font_size=16, color="#fff")
    
    timer = 0
    timer_text = canvas.create_text(10, 56, font="Helvetica", text=str(timer), color="#fff", font_size=48)
    
    player_overlap = [] # init of player overlay
    
    while True:
        # get keyboard press
        keyboard_press = canvas.get_last_key_press()
        
        if keyboard_press != None:
            # print(keyboard_press)
            coords = change_coordinates(coords, keyboard_press)
            move_player(canvas, player, coords)
    
        keyboard_press = None
        
        player_overlap = canvas.find_overlapping(coords["x"] + 10, coords["y"] + 10, coords["x"] + 70, coords["y"] + 70)
        # print("Player overlap:", player_overlap)
        
        """
        After getting the overlap, we can see the overlap objects
        "shape_12" represents the first enemy,
        "shape_17" represent the second enemy,
        and "shape_6" represents the finish line
        """
        if ("shape_12" in player_overlap or "shape_17" in player_overlap):
            canvas.create_text(10, 724, font="Helvetica", text="GAME OVER!", color="#fff", font_size=48)
            canvas.create_text(10, 774, font="Helvetica", text="You have been caught by the enemy.", color="#fff", font_size=16)
            break
        elif ("shape_6" in player_overlap):
            canvas.create_text(10, 724, font="Helvetica", text="YOU WON!", color="#fff", font_size=48)
            canvas.create_text(10, 774, font="Helvetica", text="You have reached the finish line.", color="#fff", font_size=16)
            break
        
        enemy1_coords = change_enemy_coords(enemy1_coords)
        move_player(canvas, enemy1, enemy1_coords)
        
        enemy2_coords = change_enemy_coords(enemy2_coords)
        move_player(canvas, enemy2, enemy2_coords)
        
        timer += DELAY_INTERVAL
        canvas.change_text(timer_text, str(math.floor(timer)))
        time.sleep(DELAY_INTERVAL)
        
def change_coordinates(coords, direction):
    """
    Change coordinates for the player and enemies instance
    with the new position according to direction by keyboard press
    
    input: coords: { x: int, y: int }, direction: str
    output: coords: { x: int, y: int }
    """
    
    if (direction == "ArrowLeft") and coords["x"] > 10:
        return { "x": coords["x"] - 10, "y": coords["y"] }
    elif (direction == "ArrowRight") and coords["x"] < CANVAS_WIDTH - 90:
        return { "x": coords["x"] + 10, "y": coords["y"] }
    elif (direction == "ArrowUp") and coords["y"] > 10:
        return { "x": coords["x"], "y": coords["y"] - 10 }
    elif (direction == "ArrowDown") and coords["y"] < CANVAS_HEIGHT - 90:
        return { "x": coords["x"], "y": coords["y"] + 10 }
    else:
        return { "x": coords["x"], "y": coords["y"] }
        
def change_enemy_coords(coords):
    """
    Move the enemy position horizontally
    """
    
    if (coords["x"] < 10) or (coords["x"] > CANVAS_WIDTH - 90):
        coords["movement"] *= -1
        
    return { "x": coords["x"] + coords["movement"], "y": coords["y"], "movement": coords["movement"] }
    
def draw_grass(canvas, x1, y1):
    """
    Draw a polygon grass as a game decoration
    """
    
    canvas.create_polygon(
        x1, y1,
        x1 + 5, y1 - 15,
        x1 + 10, y1 - 5,
        x1 + 15, y1 - 20,
        x1 + 20, y1 - 5,
        x1 + 25, y1 - 15,
        x1 + 30, y1,
        x1, y1,
        color="#4f772d"
    )
    
def move_player(canvas, player, coords):
    """
    Move players and enemies
    according to their coordinates
    """
    
    canvas.moveto(player["face"], coords["x"], coords["y"])
    canvas.moveto(player["left_eye"], coords["x"] + 20, coords["y"] + 20)
    canvas.moveto(player["right_eye"], coords["x"] + 50, coords["y"] + 20)

    canvas.delete(player["nose"])
    player["nose"] = canvas.create_polygon(coords["x"] + 30, coords["y"] + 50, coords["x"] + 50, coords["y"] + 50,  coords["x"] + 40, coords["y"] + 20, color="#222")

    canvas.delete(player["mouth"])
    player["mouth"] = canvas.create_polygon(coords["x"] + 30, coords["y"] + 60, coords["x"] + 50, coords["y"] + 60,  coords["x"] + 40, coords["y"] + 70, color="#222")
    
    return
        
if __name__ == '__main__':
    main()