import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    
    # start_quiz = True
    
    # # while start_quiz:
    # #     pass
    
    num1, num2 = generate_random_numbers()
    solution = get_addition_answer(num1, num2)
    
    your_answer = generate_question(num1, num2)
    
    if (your_answer == solution):
        print("Correct!")
    else:
        print("Incorrect.")
        print("The expected answer is", solution)
    
def generate_random_numbers():
    number_a = random.randint(1, 100)
    number_b = random.randint(1, 100)
    
    return number_a, number_b
    
def generate_question(a, b):
    print("What is " + str(a) + " + " + str(b) + "?")
    return int(input("Your answer: "))
    
def get_addition_answer(a, b):
    return a + b
    
    
if __name__ == '__main__':
    main()