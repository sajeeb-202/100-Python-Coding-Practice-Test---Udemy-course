def calculate_powers_of_two(n: int):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
        
    if n <= 0:
        return []

    power_of_two = lambda x: 2 ** x
    return [power_of_two(i) for i in range(n)]

# limit = int(input())
# listy = []
# for i in range(limit):
#     result = 2**i
#     listy.append(result)
# print(listy)    