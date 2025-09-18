# Quicksort
import random
import time

start_time = time.time()

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        low = []
        high = []

        for j in range(1, len(array)):
            if array[j] <= array[0]:
                low.append(array[j])
            else:
                high.append(array[j])

        return quicksort(low) + [array[0]] + quicksort(high)

nums = [random.randint(1, 10000) for _ in range(10)]
print("Unsorted list:", nums)
sorted_nums = quicksort(nums)
print("Sorted list:", sorted_nums)

end_time = time.time()
elapsed_time = end_time - start_time

print(elapsed_time)        



        