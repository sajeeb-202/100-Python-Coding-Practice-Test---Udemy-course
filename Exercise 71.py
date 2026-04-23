def delete_element_from_dict(input_dict, key):
    # Check if key exists in dictionary
    if key in input_dict:
        del input_dict[key]
    
    return input_dict