def sentence_type(entry):
    # for i in range(len(input)):
    if entry[- 1] == ".":
        return "declarative"
    elif entry[- 1] == "!":
        return "exclamatory"
    elif entry[- 1] == "?":
        return "interrogative"
    else:
        return "bad ending"

print(sentence_type(input))

def main():


entry = "This is a sentence."
# print(f"Your entry has {vowel_count(sentence)} vowels in it")
