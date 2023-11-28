# This problem is attempted for extra credit :)
words = ['apple', 'pumpkin', 'log', 'River', 'fox', 'pond']

def alphabetical(words):

    sorted_words = []

    for word in words:
        sorted_words.append(' '.join(sorted(word)))

# Then printed the original list of words
    print(f"Original: \t", ' '.join(words))
    print(f"Aplhabetical: \t", ' '.join(sorted_words))
