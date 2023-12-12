def index_of(text, a_string):
    if not(a_string in text):
        return -1
    elif len(a_string) == len(text):
        return 0
    else:
        return index_of(text[1:], a_string) + 1

print(index_of("Mississippi", "sip"))
