# Combining Dictionaries and Functions

#Calculator
from logo import calculator_logo
# Addition
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(calculator_logo)
    # To take 1st numbers inputs form the users
    num1 = float(input("What's the first number?: "))

    # To show the operation symbols
    for symbols in operations:
        print(symbols)

    should_continue = True 

    while should_continue:   
        operation_symbol = input("Pick an operation: ")

        # To take 2nd numbers inputs form the users
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'Y' to continue calculating with {answer}, or type 'N' ot start a new calculation: ") == "y": 
            num1 = answer
        else: 
            should_continue = False
            calculator()
calculator()