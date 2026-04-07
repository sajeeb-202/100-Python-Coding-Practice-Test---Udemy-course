def is_armstrong_number(number: int) -> bool:
    
    if number < 0:
        return False
    
    # Convert number to string to get digits
    digits = str(number)
    n = len(digits)
    
    total = 0
    for i in digits:
        total += int(i) ** n
        
    return total == number