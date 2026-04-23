def create_multiline_string(lines):
    # Check if input is a list
    if not isinstance(lines, list):
        return "Input must be a list of strings."
    # Check if all elements are strings
    if not all(isinstance(line, str) for line in lines):
        return "All elements in the list must be strings."

    # Join lines with newline character

    return "\n".join(lines)