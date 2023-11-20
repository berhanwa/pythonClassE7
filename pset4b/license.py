import random
import string


# Defined the random_capital function where random capital letters are generated
def random_capital():
    letters = [random.choice(string.ascii_uppercase) for _ in range (3)]
    return ''.join(letters)


# Defined the random_plate function where random numbers are generated, and with the f string, combined the letters and a space to form the overall license plates
def random_plate():
    numbers = random.randint(100, 999)
    license = f"{random_capital()} {numbers}"
    return license

# Here, the results are being printed 20 times within this for loop that has _ as the placeholder variable that gets ignored
for _ in range (20):
    print(random_plate())
