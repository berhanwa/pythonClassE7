def check(card_number):
    digits = []
    for d in str(card_number):
        digits.append(int(d))

    # Saving the 8th digit since arrays start from 0 with len(digits)-1
    check_digit = digits[len(digits)-1]

    sum_odds = 0
    doubles = []
    sum_double = 0
    odds = []

    # Finding the sum of every other digit (odds)
    for i in range (len(digits)-1, -1, -1):

        # Find digits to add up and double
        if i % 2 != 0:
            sum_odds += digits[i]
            odds.append(digits[i])

        # Multiplies double values by 2
        else:
            double = digits[i] * 2

            # If they are double digits, then splits 'double's values into single digits
            if double > 9:
                last_digit = double % 10
                first_digit = double // 10

                sum_double = sum_double = first_digit + last_digit
                # doubles.append(first_digit)

            else:
                sum_double += double
                # doubles.append(double)

    result = sum_odds + sum_double


    # Here, print the results and verify if the check digit is valid or not
    print (f"Result: {sum_odds} + {sum_double} = {result}")
    if result % 10 == 0:
        print("VALID")
    else:
        print("INVALID")
        # Finds the check_digit in order to get a valid result
        valid_result = round(result, -1) # Ensures last digit is 0 by rounding to the nearest 10
        valid_sum_odds = valid_result - sum_double # Finds the sum of odd digits w the valid check digits
        valid_check_digit = valid_sum_odds - (sum_odds - check_digit) # Finds the valid check digits by subtracting the remaining digits from valid_sum_odd

        print(f"Target check digit: {valid_check_digit}")


card_number = int(input('Provide your credit card number: '))
check(card_number)

