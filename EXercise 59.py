def print_colored_text(text, color):
    color_codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m"
    }
    
    if color not in color_codes:
        return f"Unsupported color: {color}. Please choose from {list(color_codes.keys())}."
    
    return f"{color_codes[color]}{text}\033[0m"
print_colored_text("!@#$%^&*()", "green")