def generate_fibonacci(n):
    Fibonacci_list = []
    if n<=0:
        return Fibonacci_list
        
    if n==1:
        return [0]
        
    if n==2:
        return [0,1]
           
           
    if n>2:
        a = 0
        b = 1
        summ= 0
        Fibonacci_list = [a,b]
        for i in range(n-2):
            summ = a+b
            a, b=b, a+b
            Fibonacci_list.append(summ)
            
        return Fibonacci_list        
    

    #.............Test cases.............

    test_values = int(input())
    generate_fibonacci(test_values)