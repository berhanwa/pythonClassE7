# Mental note: perfect numbers equal the sum of their positive divisors. i.e 6 is one, bc divisors 1 + 2 + 3 = 6
# Started by asking user to input the number that will determine both the height and width of the pattern

num = int(input('Enter an integer:'))
perfect_numbers = [] # Container for the perfect_numbers


def get_divisors (n): # Gets all the divisors for n
    divisors = []  # Container for the divisors
    for i in range (1, n):
        if n % i == 0:
            divisors.append(i) # Adds the i range value to the divisors
    return divisors

def is_perfect_number (n): # Checks to see if n is a perfect number by using a boolean operator
    divisors = get_divisors(n)
    return sum(divisors) == n

for i in range (1, num + 1): # Finds the perfect numbers
    if is_perfect_number(i):
        perfect_numbers.append(i) # Add perfect number to the container

for perfect in perfect_numbers: # This prints the perfect numbers
    print(perfect)
