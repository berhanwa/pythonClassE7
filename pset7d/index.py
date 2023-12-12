####  Attempted this problem for extra credit  ####


# After detailing the base case from the pset handout, checked if the length of the two parameters are equal, meaning that a_string is at the 0th index position
def index_of(text, a_string):
    if not(a_string in text):
        return -1
    elif len(a_string) == len(text):
        return 0

    # Recursively iterated through text by means of making it one character shorter (removing the 0th index position)
    # and then incremented by 1 to account for the removed element from the recursion
    else:
        return index_of(text[1:], a_string) + 1

print(index_of("Mississippi", "sip"))
print(index_of("Amron", "ron"))
