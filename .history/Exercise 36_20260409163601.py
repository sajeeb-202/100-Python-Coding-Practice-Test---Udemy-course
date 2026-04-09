def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def calculator(operation, x, y):
    if operation == "add":
        return add(x, y)
    elif operation == "subtract":
        return subtract(x, y)
    elif operation == "multiply":
        return multiply(x, y)
    elif operation == "divide":
        return divide(x, y)
    else:
        return "Error: Invalid operation"