def calculate_triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    
    area = (base * height) / 2
    return area

#........Test the function.......

Test_values = [(10,5),(7.5,3.2), (0, 5)]

for i in  range(len(Test_values)):
    try:
        result = calculate_triangle_area(*Test_values[i])
        print(f"Triangle with base {Test_values[i][0]} and height {Test_values[i][1]} has area: {result}")
    except ValueError as e:
        print(f"Error: {e}")