

def eligible_for_house (age, length_of_citizenship):
    return (age >= 25)  and (length_of_citizenship >= 7)

def eligible_for_senate (age, length_of_citizenship):
    return (age >= 30)  and (length_of_citizenship >= 9)

def main():

    age = int(input('How old are you? '))
    length_of_citizenship = int(input('How many years have you been a US citizen? '))

    if eligible_for_house (age, length_of_citizenship) and eligible_for_senate (age, length_of_citizenship):
        print ("The candidate is eligible for election to the House of Representatives AND to the Senate.")
    elif eligible_for_house(age, length_of_citizenship) or eligible_for_senate (age, length_of_citizenship):
        if eligible_for_house(age, length_of_citizenship):
            print ("The candidate is eligible for election to the House of Representatives but is NOT eligible for election to the Senate.")
        if eligible_for_senate(age, length_of_citizenship):
            print ("The candidate is eligible for election to the Senate but is NOT eligible for election to the House of Representatives.")
    else:
        print ("The candidate is NOT eligible for election to either the House of Representatives or the Senate.")
main ()

# def eligible_for_house (age, length_of_citizenship):
#     if age >= 25 and length_of_citizenship >= 7:
#         return True
