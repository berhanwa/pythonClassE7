import random

def random_capital():
    letters = random.choices(letters.ascii_uppercase)
    return letters
print (random_capital())

def random_plate():
    license = ".join( letters + " " + random.randint(100,999) )"
    return license
print (random_plate())

# string.printable
