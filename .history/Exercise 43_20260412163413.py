def sort_words_alphabetically(sentence):
    # Handle empty input
    if sentence == "":
        return ""

    # Split sentence into words
    words = sentence.split(" ")

    # Sort words case-insensitively
    sorted_words = sorted(words, key=str.lower)

    # Join back into a sentence
    return " ".join(sorted_words)