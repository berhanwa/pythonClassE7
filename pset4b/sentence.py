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

entry = str(input('Write something: '))
# entry = "This is a sentence."

def main():
    print(sentence_type(entry))
main()


# print(f"Your entry has {vowel_count(sentence)} vowels in it")
