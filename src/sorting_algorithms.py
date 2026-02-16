class Counter:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0


def bubble_sort(arr):
    counter = Counter()
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            counter.comparisons += 1
            if arr[j] > arr[j + 1]:
                counter.swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return counter

def insertion_sort(arr):
    counter = Counter()
    arr = arr.copy()
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            counter.comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                counter.swaps += 1
                j -= 1
            else:
                break
        
        arr[j + 1] = key

    return counter

def merge_sort(arr):
    counter = Counter()
    arr_copy = arr.copy()

    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            counter.comparisons += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    merge_sort_recursive(arr_copy)
    return counter

import random


def quicksort_first_pivot(arr):
    counter = Counter()
    arr_copy = arr.copy()

    def quicksort(low, high):
        if low < high:
            p = partition(low, high)
            quicksort(low, p - 1)
            quicksort(p + 1, high)

    def partition(low, high):
        pivot = arr_copy[low]
        i = low + 1

        for j in range(low + 1, high + 1):
            counter.comparisons += 1
            if arr_copy[j] < pivot:
                arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
                i += 1

        arr_copy[low], arr_copy[i - 1] = arr_copy[i - 1], arr_copy[low]
        return i - 1

    quicksort(0, len(arr_copy) - 1)
    return counter


def quicksort_random_pivot(arr):
    counter = Counter()
    arr_copy = arr.copy()

    def quicksort(low, high):
        if low < high:
            p = partition(low, high)
            quicksort(low, p - 1)
            quicksort(p + 1, high)

    def partition(low, high):
        pivot_index = random.randint(low, high)
        arr_copy[low], arr_copy[pivot_index] = arr_copy[pivot_index], arr_copy[low]

        pivot = arr_copy[low]
        i = low + 1

        for j in range(low + 1, high + 1):
            counter.comparisons += 1
            if arr_copy[j] < pivot:
                arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
                i += 1

        arr_copy[low], arr_copy[i - 1] = arr_copy[i - 1], arr_copy[low]
        return i - 1

    quicksort(0, len(arr_copy) - 1)
    return counter


