def add_two_numbers(num1, num2):
    summ = num1 + num2
    return summ

#.......Test cases........

Test_values = [(10 , 5), (-4, 9), (0, 6)]

for i in range(len(Test_values)):
    result = add_two_numbers(*Test_values[i])
    print(f"{Test_values[i][0]} and {Test_values[i][1]} sum is {Test_values[i]} ")