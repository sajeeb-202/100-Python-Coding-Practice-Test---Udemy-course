def generate_multiplication_table(number: int, limit: int = 10):
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Limit must be a positive integer.")
    
    #lines = []
    for i in range(1, limit + 1):
        lines.append(f"{number} x {i} = {number * i}")
    
    return "\n".join(lines)
print(generate_multiplication_table(2,10))