# Defined the function to go through a for loop of the paramenter sentence, where the count increments every time a vowel is found inside the loop
def vowel_count(sentence):
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count

# Specified what vowels and sentence are below, where users enter a sentence
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def main ():
    sentence = str('I think, therefore I am')
    print(f"{sentence}\n Your entry has {vowel_count(sentence)} vowels in it")

    sentence = str('Birds of a Feather Flock Together')
    print(f"\n{sentence}\n Your entry has {vowel_count(sentence)} vowels in it")

    sentence = str('Birds of a Feather Flock Together')
    print(f"\n{sentence}\n Your entry has {vowel_count(sentence)} vowels in it")
main ()

# Printed the results of the vowel_count function that lets users know the context



# sentence = str(input('Write something: '))
