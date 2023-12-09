import string
alphabet = list(string.ascii_uppercase)
print (alphabet)


def missing_letters(words):

    used_letters = set()

    for word in words:
        for char in word:
            used_letter.add(char)

    missing_letters = sorted(list(all_letters - used_letters))
    return missing_letters
