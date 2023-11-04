

print ('I will compute the sum of even integers from 2 through:')
n = int(input())
sum_even = 0

for i in range(2, n+1, 2):
    sum_even += i

print ('The sum is' " " f'{sum_even}')
