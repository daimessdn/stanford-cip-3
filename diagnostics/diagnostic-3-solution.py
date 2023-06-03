# This is one possible solution
from karel.stanfordkarel import *

# File: warmup.py
# -----------------------------
# The warmup program defines a "main"
# function which currently just has one
# Command. Add two more commands to make karel: move(),
# pick_beeper(), move()
def main():
    for i in range(3):
        make_wave()
        move()
        move()

    make_wave()

def make_wave():
    put_beeper()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()