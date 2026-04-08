def gcd(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def find_lcm(a, b):
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)