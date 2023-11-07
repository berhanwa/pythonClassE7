# Mental note: perfect numbers equal the sum of their positive divisors. i.e 6 is one, bc divisors 1 + 2 + 3 = 6
# Started by asking user to input the number that will determine both the height and width of the pattern

num = int(input('Enter an integer:'))
perfect_numbers = [] # Container for the perfect_numbers variable


def get_divisors (n):
    divisors = []  # Container for the divisors variable
    for i in range (1, n):
        if n % i == 0:
            divisors.append(i) # Adds the i range value to the divisors
    return divisors

def is_perfect_number (n):
    divisors = get_divisors(n)
    return sum(divisors) == n

for i in range (1, num + 1):
    if is_perfect_number(i):
        is_perfect_number.append(i)

for perfect in perfect_numbers:
    print(perfect)
