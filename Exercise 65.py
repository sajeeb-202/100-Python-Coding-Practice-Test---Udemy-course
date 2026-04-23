def read_file_to_list(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.rstrip('\n') for line in file]
    except FileNotFoundError:
        return []