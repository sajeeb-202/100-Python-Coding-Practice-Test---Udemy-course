def find_hcf(a: int, b: int) -> int:
    

    # Special case: both zero
    if a == 0 and b == 0:
        return 0

    # Use absolute values so that negative numbers don't cause issues
    a, b = abs(a), abs(b)

    # Euclidean Algorithm
    while b != 0:
        a, b = b, a % b

    return a