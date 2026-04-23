def is_float(string):
    # Handle None or non-string inputs
    if not isinstance(string, str):
        return False

    # Remove leading/trailing whitespace
    string = string.strip()

    # Check empty or whitespace-only string
    if string == "":
        return False

    try:
        float(string)
        return True
    except (ValueError, TypeError):
        return False