def digit_check(numbers):

    occurrences = [0] * 10

    for i in numbers:
        digit = int(i)
        occurrences[digit] += 1

        # if numbers.index(0) == 0:
        #     occurrences[digit] !=

    return occurrences

numbers = str(int(input('Please enter some numbers: ')))
print(f"Digit: 0 1 2 3 4 5 6 7 8 9 \n Occurrences: {digit_check(numbers)}\n")
