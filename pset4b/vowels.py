def vowel_count(sentence):
    # sentence.count('aeiouAEIOU')
    count = 0
    for i in range (len(sentence)):
        if "a" or "e" or "i" or "o" or "u" in sentence:
            return count += 1

        # sentence.count(x) for x in "aeiouAEIOU":
    # return vowel_count(sentence)

sentence = "I think, therefore I am"
print (vowel_count(sentence))
