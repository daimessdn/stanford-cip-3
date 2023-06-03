def main():
    # TODO write your solution here
    sequence = 1
    
    print("Enter a sequence of non-decreasing numbers.")
    
    number_1 = float(input("Enter num: "))
    number_2 = float(input("Enter num: "))
    
    while number_2 >= number_1:
        sequence += 1
        
        number_1 = number_2
        number_2 = float(input("Enter num: "))
        
    print("Thanks for playing!")
    print("Sequence length:", sequence)


if __name__ == "__main__":
    main()
