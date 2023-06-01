from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def reverse_turn():
    turn_left()
    turn_left()
    
def main():
    """
    All whole function will be executed here
    """
    
    move()
    move()
    
    pick_beeper()
    
    move()
    
    turn_left()
    for i in range(2):
        move()
    put_beeper()
    
    reverse_turn()
    for i in range(2):
        move()
        
    turn_right()
    for i in range(3):
        move()
        
    reverse_turn()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()