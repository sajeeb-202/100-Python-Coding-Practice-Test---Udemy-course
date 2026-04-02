def check_odd_even(number):
    #checking integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# .........Test the function..........

Test_values = [10, 0, -5, 7.5]

for i in range(len(Test_values)):
    try:
        result = check_odd_even(Test_values[i])
        print(f"Input: {Test_values[i]} → Output: {result}")
    except TypeError as e:
        print(f"Input: {Test_values[i]} → Error: {e}")