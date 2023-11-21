def sentence_type (input):
input = "This is a sentence."


def vowel_count(sentence):
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count

def main():



print(f"Your entry has {vowel_count(sentence)} vowels in it")
