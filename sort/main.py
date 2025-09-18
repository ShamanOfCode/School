import random
import time

# Selection sort
def selection_sort(lst):
    n = len(lst)
    comparisons = 0
    swaps = 0
    start_time = time.time()
    for i in range(n):
        minimum_number = i
        for j in range(i+1, n):
            comparisons += 1
            if lst[j] < lst[minimum_number]:
                minimum_number = j
        if i != minimum_number:
            lst[i], lst[minimum_number] = lst[minimum_number], lst[i]
            swaps += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    return comparisons, swaps, elapsed_time

# Bubble sort
def bubble_sort(lst):
    n = len(lst)
    comparisons = 0
    swaps = 0
    start_time = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swaps += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    return comparisons, swaps, elapsed_time

# Insertion sort
def insertion_sort(lst):
    n = len(lst)
    counter = 0
    for i in range(1, n):
        counter += 1
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return counter

def quicksort(array):
    start_time = time.time()
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
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

# Example list to sort
nums = [random.randint(1, 10000) for _ in range(10000)]

nums_for_selection = nums.copy()
nums_for_bubble = nums.copy()
nums_for_insertion = nums.copy()
nums_for_quicksort = nums.copy()

# Print + Time Selection Sort
selection_comparisons, selection_swaps, selection_time = selection_sort(nums_for_selection)
print("Selection sort: ", nums_for_selection)
print(f"Selection sort time: {selection_time:.6f} seconds, comparisons: {selection_comparisons}, swaps: {selection_swaps}")

# Print + Time Bubble Sort
bubble_comparisons, bubble_swaps, bubble_time = bubble_sort(nums_for_bubble)
print("Bubble sort: ", nums_for_bubble)
print(f"Bubble sort time: {bubble_time:.6f} seconds, comparisons: {bubble_comparisons}, swaps: {bubble_swaps}")

# Print + Time Insertion Sort
start = time.time()
insertion_counter = insertion_sort(nums_for_insertion)
insertion_time = time.time() - start
print("Insertion sort: ", nums_for_insertion)
print(f"Insertion sort time: {insertion_time:.6f} seconds, counter: {insertion_counter}")

# Print + Time Quicksort
start = time.time()
quicksort_counter = quicksort(nums_for_quicksort)
quicksort_time = time.time() - start
print("Quick Sort: ", nums_for_quicksort)
print(f"Quick Sort time: {quicksort_time:.6f} seconds")

print(f"Selection sort time: {selection_time:.6f} seconds, comparisons: {selection_comparisons}, swaps: {selection_swaps}")
print(f"Bubble sort time: {bubble_time:.6f} seconds, comparisons: {bubble_comparisons}, swaps: {bubble_swaps}")
print(f"Insertion sort time: {insertion_time:.6f} seconds, counter: {insertion_counter}")
print(f"Quick Sort time: {quicksort_time:.6f} seconds")