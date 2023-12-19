# Program begins by asking users to guess the word (argv)

# Iterate through each of the 6 rounds of guesses and check each char, if it's in the word, in the right place or not in there

# Return the feedback per round until the final 6th round to let users know if they won or lost

from random import *
from sys import argv

def guesses():
        word_list = []
    rounds
    with open(argv[1], 'r') as file:

        for word in file:
            word_list.append( word[0:len(word)-1] )
    # print(word_list)

print("Wordle Game Instructions")
