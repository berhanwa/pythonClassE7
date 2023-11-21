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

# In the main program, the sentence_type function's results get printed out in the different options specified from the sentence_type function
def main():
    entry = str("Example of response to a period at the end.")
    print(entry, "\n", sentence_type(entry))

    entry = str("Example of response to an exclamation at the end!")
    print(entry, "\n", sentence_type(entry))

    entry = str("Example of response to a question mark at the end?")
    print(entry, "\n", sentence_type(entry))

    entry = str("Example of response to nothing at the end")
    print(entry, "\n", sentence_type(entry))
main()


# I previously had the user is asked to enter something, and have the result printed but changed direction after seeing Ben's response in the Ed discussion
# entry = str(input('Write something: '))
