from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers infinite
her bag. How can you solve this puzzle?
"""


def main():
    # first step: move one step forward
    move_one_step()
    
    while beepers_present():
        spread_beepers_in_row()

def spread_beepers_in_row():
    pick_beeper()
    
    if no_beepers_present():
        # if the last beeper picked-up
        put_last_beeper()
    else:
        put_beeper_on_current_corner()
        move_to_piles()
        
def move_to_piles():
    return_to_start()
    move_one_step()
        
def put_beeper_on_current_corner():
    while beepers_present():
        move()
    put_beeper()

def put_last_beeper():
    put_beeper()
    return_to_start()
    
def return_to_start():
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    
def move_one_step():
    move()
        
def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()