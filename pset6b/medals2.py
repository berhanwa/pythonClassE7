# Created a dictionary that pairs the countries as keys and the different medal types won as the values
medal_counts = {
    "Canada"        : [0, 3, 0],
    "Italy"         : [0, 0, 1],
    "Germany"       : [0, 0, 1],
    "Japan"         : [1, 0, 0],
    "Kazakhstan"    : [0, 0, 1],
    "Russia"        : [3, 1, 1],
    "South Korea"   : [0, 1, 0],
    "United States" : [1, 0, 1]
}

### ATTEMPTED THE 2 EXTRA CREDIT POINTS ###
# Then made a variable to alphabetically store the sorted keys or countries of the dictionary, since the sorted() function automatically alphabetizes
sorted_countries = sorted(medal_counts.keys())

# Prints out the row of medal types and the total with the right align formatting within the f strings as the table header
print (f"{'':>15}{'Gold':>6}{'Silver':>8}{'Bronze':>8}{'Total':>8}")

# Then iterated through the counties and collected the medal count values paired to each country then sums them up to form the Total column
for country in sorted_countries:
    medals = medal_counts[country]
    total = sum(medals)

    # This second print statement completes the body of the table and with the right align formatting again
    print(f"{country:>15}{medals[0]:>6}{medals[1]:>8}{medals[2]:>8}{total:>8}")
