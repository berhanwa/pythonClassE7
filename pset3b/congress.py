age = int(input('How old are you? '))
length_of_citizenship = int(input('How many years have you been a US citizen? '))

def eligible_for_house (age, length_of_citizenship):
    if age >= 25 and length_of_citizenship >= 7:
        return True
