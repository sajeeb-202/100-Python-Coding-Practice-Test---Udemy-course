def concatenate_lists(list1, list2):
    # Validate inputs
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists.")
    
    # Concatenate and return new list
    return list1 + list2