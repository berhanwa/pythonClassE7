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
    else:
         print("Benefactors")
donor()



# def donor():
#     if n < 15:
#         return "Cheapskate!"
#     elif 15 <= n < 200:
#         return "Friends"
#     elif 200 <= n < 1000:
#         return "Supporters"
#     elif 1000 <= n < 10000:
#         return "Patrons"
#     else:
#         return "Benefactors"
# donor()
