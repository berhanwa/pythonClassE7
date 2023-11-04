
print ('Enter a year:')
y = int(input())

a = y / 19
b = y // 100, c = y % 100
d = b // 4, e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4, k = c % 4
