def extract_file_extension(filename):
    # Handle empty filename
    if not filename:
        return ""
    
    # If filename ends with a dot → no extension
    if filename.endswith('.'):
        return ""
    
    # Find the last dot
    last_dot_index = filename.rfind('.')
    
    # No dot found → no extension
    if last_dot_index == -1:
        return ""
    
    # Handle hidden files
    if last_dot_index == 0:
        # If there's no other dot, it's a hidden file without extension
        if filename.count('.') == 1:
            return filename  # case like ".json"
    
    # Extract extension
    return filename[last_dot_index:]