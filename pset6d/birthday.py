from sys import argv
from random import randint

def find_matches(birthdays):
    return len(birthdays) != len(set(birthdays))

Here, the function iterates through the days of the year and 
def simulate_birthdays(simulations, students):

    # Initialized the matches
    matches = 0

    for sim in range(simulations):

        birthdays = [randint(1, 365) for student in range(students)]
        if find_matches(birthdays):
            matches += 1

    return matches
