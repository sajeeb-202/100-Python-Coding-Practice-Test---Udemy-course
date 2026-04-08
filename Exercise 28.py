def find_divisible_numbers(numbers ,divisor : int):
    result = []
    for I in numbers:
        if I%divisor == 0:
            result.append(I)
            
            
    return result      