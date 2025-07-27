# import our custom library for calculator operations
"""Something important that you are going to remark is that is we import a custom library, 
we can treat it a python module. A module is basically a file that contains Python code, already predefined by other people, 
so we dont have to worry about each function."""

import myLibrary

# print the welcome message and the help menu
myLibrary.print_help_menu()
answer_list = []
operation = myLibrary.catch_user_input()

# continuously ask for user input and perform calculations until they choose to exit
while operation != 'e' and operation != 'E':
    myLibrary.do_calculation(operation, answer_list)
    print()
    myLibrary.print_help_menu()
    operation = myLibrary.catch_user_input()

# print the history of operations performed once the above loop ends, meaning the user pressed 'e' or 'E' to exit
print()
print('Goodbye! Here is the history of your calculations:')
for i in range(len(answer_list)):
    print(str(i+1)+ ". "+ answer_list[i])