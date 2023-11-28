# This problem is attempted for extra credit :)
words = ['apple', 'pumpkin', 'log', 'River', 'fox', 'pond']

def alphabetical(words):

    # Initialized sorted_words as an empty list
    sorted_words = []

    # Here, the for loop iterates through the parameter where the words are each sorted alphabetically with the sorted function and appended into the sorted_words list that was just initialized earlier
    for word in words:
        sorted_words.append(''.join(sorted(word)))

    # Then printed the original list of words with the similar tabbed formatting and join method to concatenate the list into strings I used in problem 8, and printed the sorted_words list in the same way
    print(f"Original: \t", ' '.join(words))
    print(f"Aplhabetical: \t", ' '.join(sorted_words))

alphabetical(words)
