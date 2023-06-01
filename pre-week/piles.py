"""
Your task: Write a program in the editor,
that makes Karel pick up all the beepers
on the first row of this world.
"""

from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    move()
    # your code here
    pick_up_beepers()
    
    move_two_steps()
    pick_up_beepers()
    
    move_two_steps()
    pick_up_beepers()
    
    move()
   
  
def move_two_steps():
    """Function for Karel to move 2 steps forward"""
    for i in range(2):
        move()
        
def pick_up_beepers():
    """Function for Karel to pick up beepers at once"""
    for i in range(10):
        pick_beeper()
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()