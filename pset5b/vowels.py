# Defined the function to go through a for loop of the paramenter sentence, where the count increments every time a vowel is found inside the loop
def vowel_count(sentence):
    count = []
    for i in sentence:
        if i in vowels:
            count += 1
    return count

# Specified what vowels and sentence are below, where users enter a sentence
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
print(vowel_count(sentence))

# Printed some example sentences along with their results from the vowel_count function, as per Ben's comment in the Ed discussion
# def main ():
#     sentence = str('I think, therefore I am')
#     print(f"{sentence}\n Your entry has {vowel_count(sentence)} vowels in it")

#     sentence = str('Birds of a Feather Flock Together')
#     print(f"\n{sentence}\n Your entry has {vowel_count(sentence)} vowels in it")

#     sentence = str('Raining Cats and Dogs')
#     print(f"\n{sentence}\n Your entry has {vowel_count(sentence)} vowels in it")
# main ()


# Previously just had the user input the sentence instead of listing out some example ones
# sentence = str(input('Write something: '))
