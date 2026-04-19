def parse_string_to_number(input_string):
    # Must be a string
    if not isinstance(input_string, str):
        return "Invalid input"
    
    input_string = input_string.strip()
    
    if input_string == "":
        return "Invalid input"
    
    # Try integer first
    try:
        return int(input_string)
    except ValueError:
        pass
    
    # Try float
    try:
        return float(input_string)
    except ValueError:
        return "Invalid input"