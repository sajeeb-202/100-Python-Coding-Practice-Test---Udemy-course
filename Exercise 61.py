def get_substring(string, start, end=None):

    if not isinstance(string, str):
        return "Invalid input type"
    
    if string == "":
        return ""
    
    try:
        if end is None:
            return string[start:]
        
        else:
            return string[start:end]
        
    except Exception:
        return ""