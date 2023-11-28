def remove_lowest(grades):
    # count = [0, 0, 0, 0, 0]
    lowest_index = grades.index(min(grades))

    grades.pop(lowest_index)

    if grades == []:
        return []
    elif len(grades) == 1:
        return grades

    return grades

grades = [23, 90, 47, 55, 88]
print("a =", remove_lowest(grades))


grades = [85]
print("a =", remove_lowest(grades))


grades = []
print("a =", remove_lowest(grades))
