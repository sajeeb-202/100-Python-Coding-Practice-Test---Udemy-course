def create_pyramid(height, char='*'):
    # invalid input check
    if height <= 0 or char == "":
        return ""
    
    pyramid = ""
    
    for row in range(1, height + 1):
        spaces = " " * (height - row)
        symbols = char * (2 * row - 1)
        pyramid += spaces + symbols
        
        if row != height:
            pyramid += "\n"
    
    return pyramid