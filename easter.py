
print ('Enter a year:')
y = float(input())


a = y / 19
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

print (a)
print (b)
print (c)
print (d)
print (e)
print (g)
print (h)
print (j)
print (k)
print (m)
print (r)
print (n)
print (p)

print ('Easter Sunday falls on' " " f'{n}/{p}/{y}')

# print ('Easter Sunday falls on day' " " f'{p} of month')
