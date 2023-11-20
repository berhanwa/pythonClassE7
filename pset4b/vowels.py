# Defined the function to go through a for loop of the paramenter sentence, where the count increments every time a vowel is found inside the loop
def vowel_count(sentence):
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count


# Specified what vowels and sentence are below, where users enter a sentence
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
sentence = str(input('Write something: '))

# Printed the results of the vowel_count function that lets users know the context
print(f"Your entry has {vowel_count(sentence)} vowels in it")
