import random
import string


def random_capital():
    letters = random.choice(string.ascii_uppercase) + for _ in range(3)
    return letters


print(random_capital())


def random_plate():
    numbers = random.randint(100, 999)
    license = f"{random_capital()} {numbers}"
    return license


print(random_plate())

# def random_plate():
#     license = ".join( letters + " " + random.randint(100,999) )"
#     return license
# print (random_plate())

# string.printable
