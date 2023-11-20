def vowel_count(sentence):
    # sentence.count('aeiouAEIOU')
    count = 0
    for i in range (len(sentence)):
        if vowels in sentence:
            return count += 1

        # sentence.count(x) for x in "aeiouAEIOU":
    # return vowel_count(sentence)

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
sentence = "I think, therefore I am"
print (vowel_count(sentence))
