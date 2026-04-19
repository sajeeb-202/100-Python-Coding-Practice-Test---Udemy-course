def slice_list(lst, start=None, end=None, step=1):
    # Validate input type
    if not isinstance(lst, list):
        return []
    
    # Step cannot be zero
    if step == 0:
        return "Step cannot be zero"
    
    n = len(lst)
    
    # Handle default step
    if step is None:
        step = 1

    # Handle default start and end based on step
    if start is None:
        start = 0 if step > 0 else n - 1
    if end is None:
        end = n if step > 0 else -n - 1

    try:
        return lst[start:end:step]
    except Exception:
        return []