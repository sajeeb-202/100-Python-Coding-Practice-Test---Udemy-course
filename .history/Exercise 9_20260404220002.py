def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    
    # Check odd numbers from 3 to sqrt(n)
    i = 3
    while i * 2 <= n:
        if n % i == 0:
            return False
        i += 2  # skip even numbers
    
    return True

#...........test cases.........

test_values = [1,6,3,0,4,88,21,7,131,69,88,900,133,851]

for i in range(len(test_values)):
    result = is_prime(*test_values)
    print(f"Input : {test_values[i]} is prime {result} ")