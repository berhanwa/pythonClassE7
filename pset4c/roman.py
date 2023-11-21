def to_arabic(roman_numeral):
    num = 0
    for i in range(0, len(roman_numeral)):

        if roman_numeral[i] == "M":
            num += 1000

        elif roman_numeral[i] == "D":
            num += 500

        # C can be placed before D and M to make 400 and 900
        elif roman_numeral[i] == "C":
            # avoid index out of range
            if i == len(roman_numeral)-1:
                num += 100
                break
            # if next char is D or M, subtract 100
            if roman_numeral[i+1] == "D" or roman_numeral[i+1] == "M":
                num -= 100
            # else add 100
            else:
                num += 100

        elif roman_numeral[i] == "L":
            num += 50

        # X can be placed before L and C to make 40 and 90
        elif roman_numeral[i] == "X":
            # avoid index out of range
            if i == len(roman_numeral)-1:
                num += 10
                break
            # if next char is L or C, subtract 10
            if roman_numeral[i+1] == "L" or roman_numeral[i+1] == "C":
                num -= 10
            # else add 10
            else:
                num += 10

        elif roman_numeral[i] == "V":
            num += 5

        # I can be placed before V and X to make 4 and 9
        elif roman_numeral[i] == "I":
            # avoid index out of range
            if i == len(roman_numeral)-1:
                num += 1
                break
            # if next char is V or X, subtract 1
            if roman_numeral[i+1] == "V" or roman_numeral[i+1] == "X":
                num -= 1
            # else add 1
            else:
                num += 1
    return num


roman_numeral1 = "LXXXVII"
roman_numeral2 = "CCXIX"
roman_numeral3 = "MCCCLIV"
roman_numeral4 = "MMDCLXXIII"
roman_numeral5 = "MCDLXXVI"

# Printing out the results
print(roman_numeral1, to_arabic(roman_numeral1))
print(roman_numeral2, to_arabic(roman_numeral2))
print(roman_numeral3, to_arabic(roman_numeral3))
print(roman_numeral4, to_arabic(roman_numeral4))
print(roman_numeral5, to_arabic(roman_numeral5))
