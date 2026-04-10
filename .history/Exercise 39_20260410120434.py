def sum_natural_numbers(n):
    #if negative then error
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Base case
    if n == 0:
        return 0
    
    # Recursion case
    return n + sum_natural_numbers(n - 1)
    
        
        