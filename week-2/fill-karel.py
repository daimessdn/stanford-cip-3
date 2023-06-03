from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    while front_is_clear():
        if left_is_clear():
            fill_row_with_karel()
        else:
            fill_last_top_row()

    
def fill_row_with_karel():
    """
    Karel fills single row by beepers
    until the end of column
    and when it finishes all single row
    it returns back to first column.
    """
    
    fill_row_step()
    return_to_first_column()
    move_to_top_row()
    
def fill_last_top_row():
    """
    Karel fills the last single row by beeper,
    but it doesn't return to the first column
    """
    
    fill_row_step()
    
def fill_row_step():
    """
    First step of Karel
    Karel fills the row by beepers until the end of column
    """
    
    while front_is_clear():
        put_beeper()
        move()
        
    # resolve the last column
    put_beeper()
    
def return_to_first_column():
    """
    Karel returns to the first column after filling the row
    """
    
    turn_around()
    while front_is_clear():
        move()
        
def move_to_top_row():
    """
    Karel moves to the upper column
    if it finishes return to the first column
    """
    
    if right_is_clear():
        turn_right()
        move()
        turn_right()
    
def turn_around():
    """
    Makes Karel turn in reverse position
    """
    
    turn_left()
    turn_left()
    
def turn_right():
    """
    Makes Karel turn right by rotating clockwise position
    """
    
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()