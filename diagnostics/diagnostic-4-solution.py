# This is one possible solution
def main():
    print("Enter a sequence of non-decreasing numbers.")
    prev_num = float(input("Enter num: "))
    sequence_length = 1
    while True:
        num = float(input("Enter num: "))
        if num < prev_num:
            break
        sequence_length += 1
        prev_num = num
    print("Thanks for playing!")
    print("Sequence length: " + str(sequence_length))


if __name__ == "__main__":
    main()