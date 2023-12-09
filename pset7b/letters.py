# Imported the string module with the alphabet set containing all the letters in uppercase
import string
alphabet = set(string.ascii_uppercase)

# In this function after initializing used letters as a set, iterated over each word and converted to uppercase as well
# and then iterated over each character inside of words to append them into used_letters
def missing_letters(words):
    used_letters = set()

    for word in words:
        word = word.upper()
        for char in words:
            if  char.isalpha():
                used_letters.add(char)

    # The assigned the unused characters to this variable by using the difference set method and made it a sorted alphabetically
    missing_letters = sorted(alphabet.difference(used_letters))
    return missing_letters

# Here, an example of words are assigned and created combined_words with the join method to account for any non-letter characters inside of words
def main():
    words = [ 'Now', 'is', 'the', 'TIME']
    combined_words = ''.join(words)
    result = missing_letters(combined_words)
    print(result)
main()
