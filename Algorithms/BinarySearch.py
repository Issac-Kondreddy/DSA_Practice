def BinarySearch(arr, target):
    low = 0
    high =  len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15
result = BinarySearch(myArray, myTarget)

if result != -1:
    print("Value",myTarget,"found at index", result)
else:
    print("Target not found in array.")


def RecursiveBinarySearch(arr, target, low, high):
    if low > high:
        return -1  # Base case: Target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Found the target
    elif arr[mid] < target:
        return RecursiveBinarySearch(arr, target, mid + 1, high)  # Search right half
    else:
        return RecursiveBinarySearch(arr, target, low, mid - 1)  # Search left half

# Sort the array before performing Binary Search
arr = [170, 45, 75, 90, 802, 24, 2, 66]
arr.sort()  # Sorting is necessary for Binary Search

targetVal = 2
result = RecursiveBinarySearch(arr, targetVal, 0, len(arr) - 1)

print(f"Target {targetVal} found at index:", result)
