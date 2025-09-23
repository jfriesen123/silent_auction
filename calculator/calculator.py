# Calculator takes 2 input values and an operand to find a result. 
# Uses function outputs to continue with calculation or start again. 
# Version 1 without referring to the video solution.

import art
print(art.logo)
# TODO: Write out the 4 operations as functions

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. The keys = associated symbol
operation_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator(n1, n2, operand):
    """Calculate a solution using user input: first_num, second_num, and operand"""
    calculation = operation_functions[operator](first_num, second_num)
    # solution = f"{first_num} {operator} {second_num} = {calculation}"
    return calculation

# Ask the user for 2 numbers and an operator
first_num = float(input("What is the first number: "))

continue_working = True

while continue_working:

    operator = input("+ \n- \n* \n/ \nPick an operation: ")
    second_num = float(input("What is the next number: "))
    answer = calculator(n1=first_num, n2=second_num, operand=operator)

    # Print the equation
    print(f"{first_num} {operator} {second_num} = {answer}")

    # Ask if they want to continue with their calculation using the previous solution
    how_to_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

    # If yes, replace the value of the first number with the previous solution
    if how_to_continue == 'y':
        first_num = answer

    # If no, ask for a new first_num
    elif how_to_continue == 'n':
        print("\n"*100, art.logo)
        first_num = float(input("What is the first number: "))

    else:
        # how_to_continue != 'y' or how_to_continue != 'n':
        continue_working = False
        print("Thank you, Goodbye")
