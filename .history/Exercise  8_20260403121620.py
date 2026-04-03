def swap_variables(a,b):
    a,b = b,a
    return (a,b)

#........test cases.......

test_cases = [(10,5), (70,-5), (12,0)]

for i in range(len(test_cases)):
    result = swap_variables(*test_cases[i])
    print(f"First number is {test_cases[i][0]} and second is {test_cases[i][1]}. swap {result}")
    