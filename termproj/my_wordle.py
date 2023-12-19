# Program begins by asking users to guess the word (argv)

# Iterate through each of the 6 rounds of guesses and check each char, if it's in the word, in the right place or not in there

# Return the feedback per round until the final 6th round to let users know if they won or lost

from random import *
from sys import argv

def load_words():
    words = []
    for line in open("words.txt"):
        items = line.strip().split()
        for item in items:
            words.append(item)
            print(item)

def play(word):
    guess = input("Enter a 5 letter word: ").lower()

    #Scenario Number One - User guesses the correct word and wins
    if guess == word:
        print("🟢🟢🟢🟢🟢")



    with open(argv[1], 'r') as file:

        for word in file:
            word_list.append( word[0:len(word)-1] )
    # print(word_list)
    winning_word = word_list[ randint(0, len(word_list))]

print("Wordle Game Instructions")


