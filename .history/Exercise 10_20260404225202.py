def is_prime(n):
    if n <= 1:
        return False
        
    if n == 2:
        return True
        
    if n % 2 == 0:
        return False 
        
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
        
    return True


def find_primes_in_interval(numbers):
   
    
    primes = []
    
    for i in numbers:
        if is_prime(i):
            primes.append(i)
            
    return primes

#............test cases..........

test_values = [10,5,2,3,48,17,69,133,131,157,68,99,97]

for j in range(len(test_values)):
    result = find_primes_in_interval(test_values)
print(f"Input {test_values} array is {result}")