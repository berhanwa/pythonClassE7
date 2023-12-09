# def draw_one_box():
#     print ('+_______+')
#     print ('|       |')
#     print ('|       |')
#     print ('|       |')
#     print ('|       |')
#     print ('+_______+')
# draw_one_box()


# print(foo)
# bar = 13
# foo = 23 - 45 // 10
# foo += 6
# bar = foo % bar
# print (foo * 2)
# print (foo + bar)
# print (foo, bar)

# stay active////

# def main():
#     print ("She said, \"", end="")
#     print ("Never put off till tomorrow... ", end="")
#     print ("\nWhat you can do")
#     print ("The day", end="")
#     print ()
#     print ("After tomorrow!\"")
# main()

# def first():
#     print("Inside first function!")

# def second():
#     first()
#     print("Inside second function!")

# def third():
#     first()
#     print("Inside third function!")
#     second()

# def main():
#     first()
#     third()
#     second()
#     third()
# main()
# print ('\n')


# for j in range (5) :
#     print (3*j-2)
# your code goes right here and nowhere else!
# so that this loop will print the following numbers, one per line:
# -2 0
# 1  1
# 4  2
# 7  3
# 10 4

# for j in range(50, -10, -8):
#     print(j)

# age = int(input('State your age:'))

# height = int(input('State your hight:'))

# weight = int(input('State your weight:'))


# def main ():
#     is_a_smoker = input('Do you smoke? ')
#     is_male = input('Are you male? ')
#     is_good_looking = input('Do you have good looks? ')
#     is_able_to_relocate = input('Are you able to move? ')
#     age = input('How old are you? ')
#     height = input('How tall are you, in inches? ')
#     weight = input('How much do you weigh? ')

#     young = (21 <= age <= 25)
#     tall = (height < 72)
#     slim = (weight < 160)

# if (young and tall and slim):
#     print ('Marry me!')
# else:
#     print ('Get Lost!')


# def main():
#    concentration = "fred"
#    fred = "computer"
#    computer = "department"
#    department = "student"
#    student = "concentration"

#    sentence(concentration, fred, department)
#    sentence(student, computer, fred)
#    sentence("Fred", "honor", computer)
#    sentence("foo", "bar", "baz")
#    sentence(fred, computer, student)

# def sentence (concentration, fred, foo):
#    print("Many a " + foo + " in the "
#                   + fred + " of " + concentration)

# main()


# def foo(x):
#     return 1 - 2*x

# print ( foo(foo(foo(foo(2)))) )

# def main():
#     mystery(-2, -6)
#     mystery(2, 3)
#     mystery(4, 8)
#     mystery(10, 31)


# def mystery(x, y):
#     s = 0
#     while x > 0 and 2*y >= x:
#         print(s, end=" ")
#         y = y - x
#         x -= 1
#         s = s + 2 * x
#         print(s)

# main()

# x = [5, 3, 5, 7, 5, "banana"]

# print ( x.count(5) )
# print ( x.index(5) )
# print ( x.index("ba") )
# print ( x[0:2] )
# print ( x[x[1]] )


# names = ["Alyssa"]

# names.insert(1, "Arpit")
# names.insert(0, "Apekshya")
# names.append("Ben")
# names.pop(3)
# names.append("Apekshya")
# names.remove("Apekshya")
# names[-1] = "Stephen"

# print(names)


# foobar = [1, 2, 3, 4, 5, 6]

# foobar = [-5, -4, -3, -2, -1]

# foobar = [5 for _ in foobar]
# foobar = [foobar[-1]] + foobar[:-1]
# foobar = [foobar[-1]] + foobar[1:-1] + [foobar[0]]
# foobar = [abs(x) for x in foobar]
# foobar = [x for index, x in enumerate(foobar) if index % 2 == 1]

# print(foobar)

# y = {}
# y['a'] = 2
# y['b'] = 3
# y['a'] = 4
# print(y['a'])

# y = { 'a' : 6, 'b' : 1, 'c' : 7}
# y.pop('b')
# y.pop('d')
# for foo in y:
#     print(foo)
# print('a' in y)
# print(6 in y)

# snacks = [ 'apple', 'orange', 'chocolate' ]
# # mystery = [ x + 's' for x in snacks ]
# mystery = { x : len(x) for x in snacks }

# print(mystery)

# def mystery(n):
#     if n <= 0:
#         return 0
#     return mystery(n // 2) + 1

# print(mystery(20))


# def recurse (a_list):
#     if a_list == []:
#         return 0
#     else:
#         return 1 + recurse(a_list[1:])

# print(recurse([4, 9, 'blah', 3.21]))

# y = set()
# y.add('a')
# y.add('a')
# print(y)

# y = { 'b', 'a', 'b', 'c' }
# y.remove('b')
# print(y)

# y = { 'a', 'b' }
# y.remove('c')
# print(y)

# letters = { 'a', 'b', 'c' }
# 'ab' in letters

# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 4, 6, 8}

# set1.discard(5)
# print(set1)

def power (x, n):
    if n == 0:
        return 1.0
    elif n % 2 == 0:
        return x * power(x, n)
    else:
        return 1.0 / power(x, n-1)

test_values = [
    (2, 0),   # 2^0 = 1
    (3, 1),   # 3^1 = 3
    (5, 2),   # 5^2 = 25
    (4, 3),   # 4^3 = 64
    (6, 4),   # 6^4 = 1296
    (7, 5),   # 7^5 = 16807
    (2, 6),   # 2^6 = 64
    (3, 7),   # 3^7 = 2187
    (5, 8),   # 5^8 = 390625
    (10, 9)   # 10^9 = 1000000000
]

for base, exponent in test_values:
    result = power(base, exponent)
    result2 = pow(base, exponent)
    print(f"{base}^{exponent} = {result} vs {result2}")
