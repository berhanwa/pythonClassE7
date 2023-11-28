# Defined the functionn by first addressing the cases where no grades are passed and if only one grade is passed with if statements
def remove_lowest(grades):

    if grades == []:
        return []
    elif len(grades) == 1:
        return grades

    # Then addressed the part where the index of the lowest grade is specified, with the help of the min() list method
    lowest_index = grades.index(min(grades))

    # Then removed said index of the lowest grade with the help of the list.pop() list method
    grades.pop(lowest_index)

    return grades


# Finally, printed out the grades listed from the PSET examples to thoroughly test the program
grades = [23, 90, 47, 55, 88]
print("a =", remove_lowest(grades))


grades = [85]
print("b =", remove_lowest(grades))


grades = []
print("c =", remove_lowest(grades))

grades = [59, 92, 93, 47, 88, 47]
print("d =", remove_lowest(grades))
