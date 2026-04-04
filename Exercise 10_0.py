def is_prime(n):
    if n<=1:
        return False
        
    if n==2:
        return True
        
    if n%2==0:
        return False 
        
    Ii =3
    while Ii*Ii<=n:
        if n%Ii==0:
            return False
        Ii +=2
    return True
        
        
    
def find_primes_in_interval(start, end):
    
    list = []
    for n in range(start, end+1):
        if is_prime(n):
            list.append(n)
    return list        
            