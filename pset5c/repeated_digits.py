def digit_check(numbers):

    occurrences = [0] * 10

    for i in numbers:
        digit = int(i)
        occurrences[digit] += 1

        # if numbers.index(0) == 0:
        #     occurrences[digit] !=

    return occurrences

numbers = str(int(input('Please enter some numbers: ')))

# Specified this variable to refer to the function above, so that I can format it inside the print statement better
outcome = digit_check(numbers)

# Used tab to get the two sets of numbers to align vertically, and \n to start a new line
# And to print out the results of the function, I used the join and map functions to
print(f"Digit: \t\t0 1 2 3 4 5 6 7 8 9 \nOccurrences: \t{' '.join(map(str, outcome))}")


