# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

MIN_RANGE = 1
MAX_RANGE = MAX_NUMBER + 1

def main():
    for i in range(MIN_RANGE, MAX_RANGE):
        odd_or_even = "odd" if i % 2 != 0 else "even"
        
        print(str(i) + " is " + odd_or_even)

if __name__ == "__main__":
    main()
