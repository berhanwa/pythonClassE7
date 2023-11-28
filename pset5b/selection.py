from time import *
import random

# Initialized values as a list with elements
values = [11,9,17,5,12]

def selection_sort(values):

    size = len(values)

    # Iterated through first loop and initialized new min values
    for i in range(0, size):
        min_val = values[i]
        min_index = i

        # And in this second loop, checked if there is a new min value
        for j in range(i + 1, size):
            if values[j] < min_val:
                min_val = values[j]
                min_index = j

        if min_index != i:
            # Storing original min as the temp
            temp_val = values[i]
            values[i] = min_val
            values[min_index] = temp_val


        # print(f"Pass {i+1}: ", min_val, " at index ", min_index)
        # print(values)
        # print()


def time_sort(n):
    values = []
    # Genrerate values
    for i in range(n):
        values.append(randint(0, 100000))

    start_time = time()
    selection_sort(values)
    end_time = time()
    print(f"Running Selection Sort for {n} random integers..")
    print('Elapsed time:', end_time-start_time, 'seconds')
    print()

time_sort(1000)
time_sort(2000)
time_sort(4000)
time_sort(8000)
time_sort(18000)
