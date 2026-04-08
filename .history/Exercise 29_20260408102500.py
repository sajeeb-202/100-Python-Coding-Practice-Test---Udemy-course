def find_factors(n):
    if not isinstance(n, int) or n < 1:
        return "Input must be a positive integer."

    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result