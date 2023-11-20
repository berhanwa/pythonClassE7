def vowel_count(sentence):
    # sentence.count('aeiouAEIOU')
    count = 0
    for i in sentence:
        if vowels in i:
            count += 1
    return count

        # sentence.count(x) for x in "aeiouAEIOU":
    # return vowel_count(sentence)

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
sentence = "I think, therefore I am"
print (vowel_count(sentence))
