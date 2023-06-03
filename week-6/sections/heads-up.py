from graphics import Canvas
import time
import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

DELAY_INTERVAL = 0.1

# def get_words_from_file():
#     """
#     This function has been implemented for you. It opens a file, 
#     and stores all of the lines into a list of strings. 
#     It returns a list of all lines in the file. 
#     """
#     with open(FILE_NAME) as f:
#         lines = f.readlines()
#         return lines

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines
        
def get_random_color():
    """
    Get random color of the text
    """
    
    colors = ["red", "salmon", "orange", "green", "blue", "magenta", "purple", "brown", "gray", "black"]
    
    return random.choice(colors)
    
def get_random_coordinates():
    """
    Get random coordinates of the text
    """
    
    x = random.randint(0, CANVAS_WIDTH - 120)
    y = random.randint(0, CANVAS_HEIGHT - 32)
    
    return x, y
    
# def fix_words(words):
#     """
#     Fix the words made from the file
#     by clearing the newline characters - specifically -
#     replacing the newline characters with empty string
#     """
    
#     for i in range(len(words)):
#         words[i] = words[i].replace("\n", "")
    
#     return words[1:]

def main():
    # your code here :) 
    # get the words list and fix it
    words = get_words_from_file()
    # print("before fixed:", words)
    
    # # words = fix_words(words)
    # print("after fixed:", words)
    
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    while True:
        # get keyboard press
        keyboard_press = canvas.get_last_key_press()
        
        # check for key press
        if keyboard_press == "Enter":
            text_x, text_y = get_random_coordinates() # get random coordinates of the text
            text_color = get_random_color()           # get random color of the text
            
            word_chosen = random.choice(words)        # get the chosen random word from the word list
            
            canvas.create_text(text_x, text_y, color=text_color, text=word_chosen, font_size=24)
    
        time.sleep(DELAY_INTERVAL)

if __name__ == '__main__':
    main()