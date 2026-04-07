def factorial(n):
    
    if n == 0 or n ==1:
        return 1
        
    elif n<0 :
        raise ValueError("Factorial is not defined for negative numbers.")  
        
    elif n>1:  
        result = 1
        for I in range(1, n+1):
            result *=I
            I +=1
        return result   