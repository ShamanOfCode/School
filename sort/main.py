nums = [100, 10, 900, 30510, -4141, 2]

# Selection sort
def selection_sort(list):
    n = len(list)

    for i in range(n):
        minimum_number = i
        for j in range(i+1, n):
            if list[j] < list[minimum_number]:
                minimum_number = j
        list[i], list[minimum_number] = list[minimum_number], list[i]

# Bubble sort
def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

# Insertion sort
def insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

# print
nums_for_selection = nums.copy()
nums_for_bubble = nums.copy()
nums_for_insertion = nums.copy()

selection_sort(nums_for_selection)
print('Selection sort:', nums_for_selection)

bubble_sort(nums_for_bubble)
print('Bubble sort:', nums_for_bubble)

insertion_sort(nums_for_insertion)
print('Insertion sort:', nums_for_insertion)
