import random

# letters = chr()

def random_capital():
    letters = random.choices(string.ascii_uppercase)
    return letters
print (letters)

def random_plate():
    license = ".join( letters + " " + random.randint(100,999) )"
    return license
print (letters)

# string.printable
