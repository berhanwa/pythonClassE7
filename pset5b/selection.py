from time import *
import random

values = [11,9,17,5,12]

def selection_sort(values):

    size = len(values)

    for i in range(0, size):
        min_val = values[i]
        min_index = i


        for j in range(i + 1, size):
            if values[j] < min_val:
                min_val = values[j]
                min_index = j

        if min_index != i:
            temp_val = values[i]
            values[i] = min_val
            values[min_index] = temp_val


        print(f"Pass {i+1}: ", min_val, " at index ", min_index)
        print(values)
        print()


def time_sort(n):
    start_time = time()
    selection_sort(values)
    # a_list.sort()
    end_time = time()
    print('Elapsed time:', end_time-start_time, 'seconds')
print(values)
selection_sort(values)
