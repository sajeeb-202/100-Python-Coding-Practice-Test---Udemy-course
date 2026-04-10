def is_palindrome(s):
    normalized = ""

    for characters in s:
        if characters.isalnum():
            normalized += characters.lower()

    return normalized == normalized[::-1]        