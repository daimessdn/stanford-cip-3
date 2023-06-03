from karel.stanfordkarel import *

def main():
    while front_is_clear():
        create_single_wave()
        move_after_create_wave()
    
def create_single_wave():
    put_beeper()
    move()
    put_beeper()

    turn_left()
    move()
    put_beeper()
    
def move_after_create_wave():
    turn_around()
    move()
    turn_left()
    
    if front_is_clear():
        move()
        move()
    
def turn_right():
    """
    Turns Karel right
    """
    
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    """
    Turns Karel around
    """
    
    turn_left()
    turn_left()

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
