import string
alphabet = set(string.ascii_letters)


def missing_letters(words):

    used_letters = set()

    for word in words:
        for char in word:
            used_letters.add(char)

    missing_letters = sorted(list(alphabet - used_letters))
    return missing_letters

def main():
    words = [ 'Now', 'is', 'the', 'TIME']
    result = missing_letters(words)
    print(result)
main()
