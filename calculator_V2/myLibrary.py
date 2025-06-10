## Tujenge--programming class
## user calculator library in which we define all the functions that we need to use in our calculator program

## menu function
def print_help_menu():
    "This function prints the help menu for the calculator."
    print()
    print("Welcome. Please select a calculation to perform by inputting the appropriate letter.")
    print("To do addition, input: a or A")
    print("To do subtraction, input: s or S")
    print("To do multiplication, input: m or M")
    print("To do division, input: d, or D")
    print("To exit, please press: e, or E")

# add function with all the typos handled
def add(history):
    "This function takes two numbers as user input, stores them in 2 variables and returns their sum. output format: x + y = z"
    print("You selected addition.")
    a = catch_number_input()
    b = catch_number_input()
    expression = str(a) + " + " + str(b) + " = " + str(a + b)
    history.append(expression) # 'append' is a list method of python list, which add a new item to the end of the list
    print(expression)

# subtract function with all the typos handled
def subtract(history):
    "This function takes two numbers as user input, stores them in 2 variables and returns their difference. output format: x - y = z"
    print("You selected subtraction.")
    a = catch_number_input()
    b = catch_number_input() 
    expression = str(a) + " - " + str(b) + " = " + str(a - b)
    history.append(expression)  
    print(expression)
    
# multiply function with all the typos handled
def multiply(history):
    "This function takes two numbers as user input, stores them in 2 variables and returns their product. # output format: x * y = z"
    print("You selected multiplication.")
    a = catch_number_input()
    b = catch_number_input()
    expression = str(a) + " * " + str(b) + " = " + str(a * b)
    history.append(expression)       
    print(expression)

# divide function with all the typos handled
def divide(history):
    "This function takes two numbers as user_input, stores them in 2 variables and returns their quotient. output format: x / y = z"
    print("You selected division.")
    a = catch_number_input()
    b = catch_number_input() 
    # Check if b is zero to avoid division by zero error
    while b == 0:
        print("ValueError: cannot divide by zero!")
        b = catch_number_input()

    expression = str(a) + " / " + str(b) + " = " + str(a / b)
    history.append(expression)
    print(expression)

def do_calculation(operation, history):  
    "This function takes a user input and calls the appropriate function to perform the calculation."
    if operation == 'a' or operation == 'A':
        add(history)

    elif operation == 's' or operation == 'S':
        subtract(history)

    elif operation == 'm' or operation == 'M':
        multiply(history)

    elif operation == 'd' or operation == 'D':
        divide(history)

# catch operation inputErrors from user and handle all the typos
def catch_user_input():
    user_input = input("Please enter a letter: ")
    while user_input not in ['a', 'A', 's', 'S', 'm', 'M', 'd', 'D', 'e', 'E']:
        print("Invalid input. Please enter a valid letter.")
        user_input = input("Please enter a letter: ")

    return user_input

## catch numbers inputErrors from user and handle all the typos
def catch_number_input():
    try:
        number = float(input("Please enter a number: "))
        return number
    except :
        print("Invalid input. Please enter a number.")
        return catch_number_input()