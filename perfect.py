# Mental note: perfect numbers equal the sum of their positive divisors. i.e 6 is one, bc divisors 1 + 2 + 3 = 6
# Started by asking user to input the number that will determine both the height and width of the pattern

num = int(input('Enter an integer:'))
perfect_numbers =


def get_divisors (n):
    divisors = []
    for i in range (1, n)
        if n % i == 0:
            
