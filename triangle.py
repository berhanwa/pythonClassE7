# Use nested loops. Specified i to be the rows, whcih increment by 100
# And specified j to be the columns, which increases by even numbers

# In the rows loop, set the range to be from 1 -> 10, because the diagram only shows 900 as the last row
for i in range (1, 10):
    line = "" # Makes the loop start fresh when it gets to this point
    for j in range (0, i):
        line += " " + str(i * 100 + (2 * j * (i - 1))) # Add then assign (+=) the string concatenation of rows by 100 with the even numbers of j multiplied with
    print (line)
# The difference in column values increases by even numbers that grow as the column number increases.
