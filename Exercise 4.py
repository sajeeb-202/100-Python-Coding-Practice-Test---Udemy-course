import math

def find_square_root(number):
    #Computes square root using math.sqrt()
    if number < 0:
        return None
    return math.sqrt(number)


def find_square_root_newton(number, precision=0.00001):
    #Computes square root using Newton-Raphson method.

    if number < 0:
        return None
    
    if number == 0:
        return 0.0

    # Initial guess
    x = number

    while True:
        root = 0.5 * (x + number / x)

        # Stop when difference is very small
        if abs(root - x) < precision:
            return root

        x = root


# ----------- Testing the functions -----------


test_values = [4, 9, 16, 2, 0, -1]

print("Using math.sqrt():")
for val in test_values:
    print(f"Square root of {val} = {find_square_root(val)}")

print("\nUsing Newton-Raphson method:")
for val in test_values:
    print(f"Square root of {val} = {find_square_root_newton(val)}")