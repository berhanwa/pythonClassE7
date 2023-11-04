# After adding the print statement asking users to enter a number, I assigned n to be the input and created the variable for the sum to be used later
print ('I will compute the sum of even integers from 2 through:')
n = int(input())
sum_even = 0

# In the for loop, I specified the range up to n+1 and that values increment by 2 each time
for i in range(2, n+1, 2):
    sum_even += i

print ('The sum is' " " f'{sum_even}')
