## Tujenge--programming class
## user calculator

## This is a simple calculator program that performs basic arithmetic operations.
def print_help_menu():
    "This function prints the help menu for the calculator."

    print("Welcome. Please select a calculation to perform by inputting the appropriate letter.")
    print("To do addition, input: a or A")
    print("To do subtraction, input: s or S")
    print("To do multiplication, input: m or M")
    print("To do division, input: d, or D")
    print("To exit, please press: e, or E")
    print("To call the help menu, please press: h, or H")

# add function 
def add(history):
    "This function takes two numbers as user input, stores them in 2 variables and returns their sum. output format: x + y = z"
    print("You selected addition.")
    a = catch_number_input()
    b = catch_number_input()
    expression = str(a) + " + " + str(b) + " = " + str(a + b)
    history.append(expression) # 'append' is a list method of python list, which add a new item to the end of the list
    print(expression)

# subtract function
def subtract(history):
    "This function takes two numbers as user input, stores them in 2 variables and returns their difference. output format: x - y = z"
    print("You selected subtraction.")
    a = catch_number_input()
    b = catch_number_input() 
    expression = str(a) + " - " + str(b) + " = " + str(a - b)
    history.append(expression)  
    print(expression)

# multiply function    
def multiply(history):
    "This function takes two numbers as user input, stores them in 2 variables and returns their product. # output format: x * y = z"
    print("You selected multiplication.")
    a = catch_number_input()
    b = catch_number_input()
    expression = str(a) + " * " + str(b) + " = " + str(a * b)
    history.append(expression)       
    print(expression)

# divide function   
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
   
# 
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

# helper function that helps with catch user typos recursion way
def catch_user_input():
    user_input = input("Please enter a letter: ")
    if user_input in ['a', 'A', 's', 'S', 'm', 'M', 'd', 'D', 'e', 'E']:
        return user_input
    elif user_input in ['h', 'H']:
        print_help_menu()
        print()
        return catch_user_input()
    else:
        print("Invalid input. Please enter a letter.")
        return catch_user_input()
    
## helper function that helps with catching number input errors
def catch_number_input():
    try:
        number = float(input("Please enter a number: "))
        return number
    except :
        print("Invalid input. Please enter a number.")
        return catch_number_input()


# # main program starts here
print_help_menu()
operation = catch_user_input()
op_history_list = [] ## store the history of operations

# keep looping/doing operations the user decides to exit (by pressing e or E))
while operation != 'e' and operation != 'E':
    do_calculation(operation, op_history_list)
    print()
    print_help_menu()
    operation = catch_user_input()
    
# when the user press e or E, stop the program and show the list of operations you have done earlier
print("Goodbye!")
print("Here is the history of your operations:")
for i in range(len(op_history_list)):
    print(str(i+1) + '. ' + op_history_list[i])
