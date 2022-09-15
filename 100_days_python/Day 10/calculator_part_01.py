# Combining Dictionaries and Functions

#Calculator

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

# To take 1st numbers inputs form the users
num1 = int(input("What's the first number?: "))

# To show the operation symbols
for symbols in operations:
    print(symbols)
    
operation_symbol = input("Pick an operation from the line above: ")

# To take 2nd numbers inputs form the users
num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

ope