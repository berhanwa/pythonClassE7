def digit_check(numbers):

    # Initialized the occurences list and multiplied by 10 since there will be 10 values inside
    occurrences = [0] * 10

    # Here, the for loop iterates through the parameter where the elements are assigned to integers and are then incremented inside the occurrences loop
    for i in numbers:
        digit = int(i)
        occurrences[digit] += 1

    return occurrences

numbers = str(int(input('Please enter some numbers: ')))

# Specified this variable to refer to the function above, so that I can format it inside the print statement better
outcome = digit_check(numbers)

# Used tab to get the two sets of numbers to align vertically, and \n to start a new line
# And to print out the results of the function, I used the join and map functions to convert the elements of outcome as strings with spaces in between
print(f"Digit: \t\t0 1 2 3 4 5 6 7 8 9 \nOccurrences: \t{' '.join(map(str, outcome))}")


