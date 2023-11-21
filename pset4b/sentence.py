# The user is asked to enter something, which gets passed into the sentence_type function below
entry = str(input('Write something: '))

# Here, the if statements go through each option of what the parameter's last value is, and has the respective option returned
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


# In the main program, the sentence_type function's results get printed out
def main():
    print(sentence_type(entry))
main()
