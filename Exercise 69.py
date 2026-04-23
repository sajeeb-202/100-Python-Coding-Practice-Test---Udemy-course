import random

def randomly_select_element(input_list):
    # Return None if the list is empty
    if not input_list:
        return None
    
    # Randomly select and return an element
    return random.choice(input_list)