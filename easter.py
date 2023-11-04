# Started by asking the user to input a year and assign that to the variable y, making sure to specify it as an int data type
print ('Enter a year:')
y = int(input())

# Then going down the numbered list by assigning the appropriate equations to the corresponding variables
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32

# I printed out each variable, because I kept getting the wrong number for 'p' at the end. Turns out I had used the wrong operator on a, so seeing everything laid out like this helped me problem-solve
# print (a)
# print (b)
# print (c)
# print (d)
# print (e)
# print (g)
# print (h)
# print (j)
# print (k)
# print (m)
# print (r)
# print (n)
# print (p)

# Finally, printed what day Easter falls on by leveraging the n, p and y values
print ('Easter Sunday falls on' " " f'{n}/{p}/{y}')
