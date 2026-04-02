import math

def solve_quadratic(a, b, c):

    # Case 1: Linear or degenerate cases (a = 0)
    if a == 0:
        if b == 0 and c == 0:
            return "Infinite solutions"
        elif b == 0 and c != 0:
            return "No solution"
        else:
            # Linear equation: bx + c = 0
            x = -c / b
            return (x,)

    # Case 2: Quadratic equation (a != 0)
    discriminant = b*b - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        # Sorting to ensure consistent order
        return tuple(sorted((x1, x2)))

    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)

    else:
        return "No real roots"