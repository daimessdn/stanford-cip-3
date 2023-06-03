# This is one possible solution
def main():
    user_height = float(input("Enter your height in meters: "))
    if user_height > 1.6 and user_height < 1.9:
        print("Correct height to be an astronaut")
    elif user_height <= 1.6:
        print("Below minimum astronaut height")
    else:
        print("Above maximum astronaut height")

if __name__ == "__main__":
    main()