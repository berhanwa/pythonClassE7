# Defined the function to go through a for loop of the paramenter sentence, where the count increments every time a vowel is found inside the loop
def vowel_count(sentence):
    count = [0, 0, 0, 0, 0]
    for letter in sentence:

        if letter == "a" or letter == "A":
            count[0] += 1
        elif letter == "e" or letter == "E":
            count[1] += 1
        elif letter == "i" or letter == "I":
            count[2] += 1
        elif letter == "o" or letter == "O":
            count[3] += 1
        elif letter == "u" or letter == "U":
            count[4] += 1

    return count

# Specified what vowels and sentence are below, where users enter a sentence


# Printed some example sentences along with their results from the vowel_count function
def main ():
    sentence = 'I think, therefore I am'
    print(f"{sentence}\n Your entry has the vowels 'aeiou' listed {vowel_count(sentence)} many times respectively \n")

    sentence = 'Birds of a Feather Flock Together'
    print(f"{sentence}\n Your entry has the vowels 'aeiou' listed {vowel_count(sentence)} many times respectively \n")

    sentence = 'Raining Cats and Dogs'
    print(f"{sentence}\n Your entry has the vowels 'aeiou' listed {vowel_count(sentence)} many times respectively")

main ()
