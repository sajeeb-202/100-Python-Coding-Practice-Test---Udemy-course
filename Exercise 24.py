def get_ascii_value(character):
    
    # Must be a string of length exactly 1
    if not isinstance(character, str) or len(character) != 1:
        return "Input must be a single character"
    
    return ord(character)