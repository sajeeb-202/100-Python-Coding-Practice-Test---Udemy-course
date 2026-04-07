def sum_of_natural_numbers(n: int):
    if not isinstance(n, int) or n <= 0:
        return "Input must be a positive integer"
    
    return n * (n + 1) / 2  # integer result