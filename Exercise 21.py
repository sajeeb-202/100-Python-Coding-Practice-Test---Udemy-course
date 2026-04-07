def is_armstrong(number: int) -> bool:

    if number < 0:
        return False  # negative numbers can't be Armstrong numbers
    
    digits = str(number)
    n = len(digits)
    sum_of_powers = 0
    
    for digit in digits:
        sum_of_powers += int(digit) ** n
    
    return sum_of_powers == number


def find_armstrong_numbers(start: int, end: int) -> list[int]:
    
    if start >= end:
        return []  # invalid range
    
    armstrong_list = []
    
    for num in range(start, end):
        if is_armstrong(num):
            armstrong_list.append(num)
    
    return armstrong_list