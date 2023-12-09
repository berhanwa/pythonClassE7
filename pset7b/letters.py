import string
alphabet = set(string.ascii_letters)
used_letters = set()

def missing_letters(words):

    for word in words:
        word = word.upper()
        for char in word:
            used_letters.add(char)

    missing_letters = sorted(alphabet.difference(used_letters))
    # missing_letters = sorted(alphabet - used_letters)
    return missing_letters
    # return [letter.upper() for letter in missing_letters]

def main():
    words = [ 'Now', 'is', 'the', 'TIME']
    result = missing_letters(words)
    print(result)
main()
