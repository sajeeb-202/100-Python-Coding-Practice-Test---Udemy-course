from datetime import datetime

def convert_string_to_datetime(date_string, date_format):

    if date_string is None or date_string == "":
        return "Invalid date string or format"
    
    try:
        return datetime.strptime(date_string, date_format)
    
    except (ValueError, TypeError):
        return "Invalid date string or format"