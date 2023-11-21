# The if statements go through each option of what the parameter's last value is, and has the respective option returned
def sentence_type(entry):
    if entry[-1] == ".":
        return "declarative"
    elif entry[-1] == "!":
        return "exclamatory"
    elif entry[-1] == "?":
        return "interrogative"
    else:
        return "bad ending"

def main():
    entry = str(input("Example of response to a period at the end."))
    sentence_type(entry)
    print(sentence_type(entry))

    entry = str(input("Example of response to an exclamation at the end!"))
    sentence_type(entry)
    print(sentence_type(entry))

    entry = str(input("Example of response to a question mark at the end?"))
    sentence_type(entry)
    print(sentence_type(entry))

    entry = str(input("Example of response to nothing at the end"))
    sentence_type(entry)
    print(sentence_type(entry))


main()

    # for i in range(len(input)):

# In the main program, the sentence_type function's results get printed out in a few examples
# The user is asked to enter something, which gets passed into the sentence_type function below


    # entry = str(input('Write something: '))
