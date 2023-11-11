age = int(input('How old are you? '))
length_of_citizenship = int(input('How many years have you been a US citizen? '))

def eligible_for_house (age, length_of_citizenship):
    return (age >= 25)  and (length_of_citizenship >= 7)

def eligible_for_senate (age, length_of_citizenship):
    return (age >= 30)  and (length_of_citizenship >= 9)

def main():
    if eligible_for_house() and eligible_for_senate () True:
        print ("The candidate is NOT eligible for election to either the House of Representatives or the Senate.")
    else:
        print ("The candidate is eligible for election to the House of Representatives")


# def eligible_for_house (age, length_of_citizenship):
#     if age >= 25 and length_of_citizenship >= 7:
#         return True
