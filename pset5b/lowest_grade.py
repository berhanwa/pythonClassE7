def remove_lowest(grades):
    # count = [0, 0, 0, 0, 0]
    lowest_index = grades.index(min(grades))

    grades.pop(lowest_index)

    return grades

grades = [23, 90, 47, 55, 88]
print("a =", grades)
