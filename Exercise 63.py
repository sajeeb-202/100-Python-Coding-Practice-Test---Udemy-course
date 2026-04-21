def print_without_newline(strings):
    # Validate input type (optional but safer)
    if not isinstance(strings, list):
        return ""
    
    # Handle empty list
    if not strings:
        return ""
    
    # Concatenate without spaces or newlines
    return "".join(strings)