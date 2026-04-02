def check_odd_even(number):
    #checking integer number
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
#.........test the function........

Test_values = [10, 0, -5, 7.5]
for i in range(len(Test_values)):
    result = check_odd_even(Test_values[i])
    print(f"Input : {Test_values[i]} = Output : {result}")