def index_of(text, a_string):
    if not(a_string in text):
        return -1
    else:
        return text.startswith(a_string) + index_of(text[1:], a_string)

print(index_of("Mississippi", "sip"))
