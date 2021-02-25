"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    operation = input("Enter your equation > ") # + 1 2
    operation_list = operation.split(" ") # gives a list [+, 1, 2]
    if operation_list[0] == "q":
        break 
    elif operation_list[0] == "+":
        print(add(int(operation_list[1]), int(operation_list[2])))
    elif operation_list[0] == "-":
        print(subtract(int(operation_list[1]), int(operation_list[2])))
    elif operation_list[0] == "*":
        print(multiply(int(operation_list[1]), int(operation_list[2])))
    elif operation_list[0] == "/":
        print(divide(int(operation_list[1]), int(operation_list[2])))
    elif operation_list[0] == "square":
        print(square(int(operation_list[1])))
    elif operation_list[0] == "cube":
        print(cube(int(operation_list[1])))
    elif operation_list[0] == "power":
        print(power(int(operation_list[1]), int(operation_list[2])))
    elif operation_list[0] == "mod":
        print(mod(int(operation_list[1]), int(operation_list[2])))
    


# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens
#             (...etc.)