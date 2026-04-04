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


def find_primes_in_interval(start, end):
    # Ensure correct order using sorted()
    start, end = sorted([start, end])
    
    primes = []
    
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
            
    return primes

#............test cases..........

test_values = [(10,2,4,3,8,15),
               (23,89,20,0,14,-32),
               (78,955,21,57,63,10)]

for j in range(len(test_values)):
    result = find_primes_in_interval(test_values[j])
    print(f"Input {test_values[j]} array is {result}")