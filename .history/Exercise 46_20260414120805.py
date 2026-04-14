import os

def safely_create_nested_directory(path):
    # Step 1: Check for empty path
    if not path:
        return False

    try:
        # Step 2: Create directory safely
        os.makedirs(path, exist_ok=True)
        return True

    except Exception:
        # Step 3: Handle any error gracefully
        return False
        