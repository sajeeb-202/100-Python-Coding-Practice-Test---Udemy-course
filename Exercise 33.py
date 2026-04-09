def decimal_to_binary(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
        
        
    if n<0:
        raise ValueError("Input must be a non-negative integer.")
        
        
    binary = bin(n)[2:]  
    return binary
        
        
          