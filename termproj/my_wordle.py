# Program begins by asking users to guess the word

# Iterate through each of the 6 rounds of guesses and check each char, if it's in the word, in the right place or not in there

# Return the feedback per round until the final 6th round to let users know if they won or lost

def load_words():
    words = []
    for line in open("words.txt"):
        items = line.strip().split()
        for item in items:
            words.append(item)
            print(item)
    return words

def play(word):
    guess = input("Enter a 5 letter word: ").lower()

    #Scenario Number One - User guesses the correct word and wins
    if guess == word:
        print("🟢🟢🟢🟢🟢")
        for i in range(0, len(word)):
            print(word[i].upper(), end = " ")
        print()
        return True
    else:
        result = ""
        letters = " "
        for i in range(0, len(word)):

            #Scenario Number Two - User guesses a word with letters in the correct positions
            if guess[i] == word[i]:
                result += "🟢"
                letters += guess[i].upper() + " "

            #Scenario Number Three - User guesses a word with letters not in the correct positions
            elif guess[i] in word:
                result += "🟡"
                letters += guess[i].upper() + " "

            #Scenario Number Four - User guesses a word with incorrect letters
            else:
                result += "🔴"
                letters += guess[i].upper() + " "

        print(result)
        # print(letters)

def main():
    import random
    words = load_words()

    word = random.choice(words).lower()

    guesses = 6
    while guesses > 0:
        if play(word):
            print("You win")
            break
        else:
            guesses -= 1
            print("You have %d guesses remaining" % guesses)
            print()
            print("_________________________________")

    if guesses == 0:
        word[0] = word[0].upper()
        print("You lost. The correct word was %s." %word)

main()

# print("Wordle Game Instructions")


