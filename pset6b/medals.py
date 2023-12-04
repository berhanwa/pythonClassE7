MEDALS = 3
COUNTRIES = 8

# Create a list of country names
countries = [
    "Canada", "Italy", "Germany", "Japan",
    "Kazakhstan", "China", "South Korea", "United States"
]

# Create a table of medal counts
counts = [
    [0, 3, 0],
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0],
    [0, 0, 1],
    [3, 1, 1],
    [0, 1, 0],
    [1, 0, 1]
]

# Prints out the row of medal types and the total with the right align formatting within the f strings as the table header
print (f"{'':>15}{'Gold':>6}{'Silver':>8}{'Bronze':>8}{'Total':>8}")

# This for loop iterates through the range of length of countries to assign the variable country at each index and also assign the
# variable medal_count to the indexes of the elements within counts, then sums them up and assigns total as that variable
for i in range (len(countries)):
    country = countries[i]
    medal_count = counts[i]
    total = sum(medal_count)

    # This second print statement completes the body of the table and with the right align formatting again
    print(f"{country:>15}{medal_count[0]:>6}{medal_count[1]:>8}{medal_count[2]:>8}{total:>8}")
