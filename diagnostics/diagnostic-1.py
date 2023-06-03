ASTRONAUT_MIN_HEIGHT = 1.6
ASTRONAUT_MAX_HEIGHT = 1.9

def main():
    # get astronaut height from user input
    astronaut_height = float(input("Enter your height in meters: "))
    
    if astronaut_height <= ASTRONAUT_MIN_HEIGHT:
        print("Below minimum astronaut height")
    elif astronaut_height >= ASTRONAUT_MAX_HEIGHT:
        print("Above maximum astronaut height")
    else:
        print("Correct height to be an astronaut")

if __name__ == "__main__":
    main()
