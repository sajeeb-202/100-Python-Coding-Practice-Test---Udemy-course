import string
import unicodedata
 
def remove_punctuations(input_string):

    # Combine ASCII punctuation and additional Unicode punctuation
    punctuation = string.punctuation + "¡¿"
    
    # Use a list comprehension to filter out punctuation while preserving whitespace
    cleaned_string = ''.join(
        char if char not in punctuation and not unicodedata.category(char).startswith('P') else ' ' if char.isspace() else ''
        for char in input_string
    )
    
    # Replace multiple spaces with a single space to clean up the output
    cleaned_string = ' '.join(cleaned_string.split())
    
    return cleaned_string