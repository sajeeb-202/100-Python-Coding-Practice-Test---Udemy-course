def handle_exceptions(input_value):
    try:
        result = 10 / input_value
        return result
    except (ZeroDivisionError, TypeError) as e:
        return f"Error: {e}"