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

