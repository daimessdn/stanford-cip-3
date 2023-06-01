from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def put_five_beepers():
    for i in range(5):
        put_beeper()
        
        if front_is_clear():
            move()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_four_steps():
    for i in range(4):
        move()

def main():
    turn_left()
    
    put_five_beepers()
    turn_right()
    move_four_steps()
    
    turn_right()
    put_five_beepers()
    
    turn_left()
    move_four_steps()
    
    turn_left()
    put_five_beepers()
    
    turn_right()
    move_four_steps()
    
    turn_right()
    put_five_beepers()
    
    turn_left()

if __name__ == '__main__':
    main()