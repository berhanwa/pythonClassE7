# print ('Enter the amount of a contribution:')
n = float(input('Enter the amount of a contribution:'))


def donor():
    if n < 15:
        print("Cheapskate!")
    elif 15 <= n < 200:
        print("Friends")
    elif 200 <= n < 1000:
        print("Supporters")
    elif 1000 <= n < 10000:
        print("Patrons")
    elif n <= 10000:
         print("Benefactors")
    else:
         print("Benefactors")
    break
donor()


# def donor():
#     if n < 0:
#         print("Error, please donate a REAL amount (i.e. no coins)!")
#     elif 0 <= n < 15:
#         print("Cheapskate!")
#     elif 15 <= n < 200:
#         print("Friends")
#     elif 200 <= n < 1000:
#         print("Supporters")
#     elif 1000 <= n < 10000:
#         print("Patrons")
#     else:
#          print("Benefactors")
# donor()



# def donor():
#     if n < 15:
#         print("Cheapskate!")
#     elif 15 <= n < 200:
#         print("Friends")
#     elif 200 <= n < 1000:
#         print("Supporters")
#     elif 1000 <= n < 10000:
#         print("Patrons")
#     else:
#          print("Benefactors")
# donor()
