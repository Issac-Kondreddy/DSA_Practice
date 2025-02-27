def partition(a, low, high):
    pivot = a[low]
    a[low], a[high] = a[high], a[low]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]
    return i + 1


def quicksort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        quicksort(a, low, p-1)
        quicksort(a, p+1, high)

test1 = [10, 80, 30, 90, 40, 50, 70]
quicksort(test1, 0, len(test1) - 1)
print(test1)  # Expected: [10, 30, 40, 50, 70, 80, 90]

test2 = [3, 3, 3, 3, 3]
quicksort(test2, 0, len(test2) - 1)
print(test2)  # Expected: [3, 3, 3, 3, 3] (Already sorted)

test3 = [1, 2, 3, 4, 5, 6]
quicksort(test3, 0, len(test3) - 1)
print(test3)  # Expected: [1, 2, 3, 4, 5, 6] (Already sorted)

test4 = [6, 5, 4, 3, 2, 1]
quicksort(test4, 0, len(test4) - 1)
print(test4)  # Expected: [1, 2, 3, 4, 5, 6] (Reverse sorted case)
