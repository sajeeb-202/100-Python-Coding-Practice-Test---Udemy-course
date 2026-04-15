def iterate_dictionary(input_dict):
    # Check if input is a dictionary
    if not isinstance(input_dict, dict):
        return "Input must be a dictionary"
    
    result = []
    
    # Iterate over key-value pairs
    for key, value in input_dict.items():
        result.append(f"{key}: {value}")
    
    return result