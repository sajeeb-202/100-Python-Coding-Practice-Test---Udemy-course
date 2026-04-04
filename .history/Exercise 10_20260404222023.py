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
        if is_prime(n):
            primes.append(n)
            
    return primes