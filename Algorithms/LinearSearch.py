def LinearSearch(arr, num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    return -1

arr = [3, 7, 2, 9, 5]
targetVal = 9

print(LinearSearch(arr, targetVal))