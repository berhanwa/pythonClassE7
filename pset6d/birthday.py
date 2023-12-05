from sys import argv
from random import randint

def find_matches(birthdays):
    return len(birthdays) != len(set(birthdays))

# Here, the function iterates through the days of the year and if birthday matches are found, the matches variable gets incremented
def simulate_birthdays(simulations, students):

    # Initialized the matches
    matches = 0

    for sim in range(simulations):

        birthdays = [randint(1, 365) for student in range(students)]
        if find_matches(birthdays):
            matches += 1

    return matches

def main():
    if len(argv) != 3:
        print("Please provide the number of simulations to run and the number of students in the class: ")
    else:
        simulations = int(argv[1])
        students = int(argv[2])

        matches = simulate_birthdays(simulations, students)

        print(f"After {simulations} simulations")
        print(f"With {students} students")
        print(f"there were {matches} simulations with at least one match")

main()
