import string
alphabet = set(string.ascii_uppercase)

def missing_letters(words):
    used_letters = set()

    for word in words:
        word = word.upper()
        for char in word isalpha():
            used_letters.add(char)
            # alphabet_cap = alphabet.upper()

    missing_letters = sorted(alphabet.difference(used_letters))
    # missing_letters = sorted(alphabet - used_letters)
    return missing_letters
    # return [letter.upper() for letter in missing_letters]

def main():
    words = [ 'Now', 'is', 'the', 'TIME']
    result = missing_letters(words)
    print(result)
main()
