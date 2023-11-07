# Started by asking users to enter the amount they wish to donate
n = float(input('Enter the amount of a contribution:'))

# Defined a function that lists out all the donor ranges, and if they enter an amount less than 0, an 'error' message will be printed out.
def donor():
    if n < 0:
        print("Error, please donate a REAL amount!")
    elif 0 <= n < 15:
        print("Cheapskate!")
    elif 15 <= n < 200:
        print("Friends")
    elif 200 <= n < 1000:
        print("Supporters")
    elif 1000 <= n < 10000:
        print("Patrons")
    else:
         print("Benefactors")
donor()
