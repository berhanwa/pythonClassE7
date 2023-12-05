from sys import argv
from random import randint

def find_matches(birthdays):
    return len(birthdays) != len(set(birthdays))
