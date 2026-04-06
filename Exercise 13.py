import random

def generate_random_number(start : int, end : int):
    X = random.randint(start, end)
    if start > end:
        raise ValueError("start value must be less than or equal to end valu")
      
      
    return X        
      
      
      
      