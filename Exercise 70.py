def append_to_file(file_path, text):
    try:
        # Open file in append mode ('a') → creates file if it doesn't exist
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(text)
        return True
    except Exception:
        return False