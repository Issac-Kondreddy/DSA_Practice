def RadixSort(arr):
    max_num = max(arr)
    place = 1
    while max_num //place > 0:
        countsort(arr, place)
        place *= 10


def countsort(arr, place):
    count = [0] * 10
    output_arr = [0] * len(arr)
    for i in arr:
        digit = (i//place) % 10
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    for i in range(len(arr)-1, -1, -1):
        digit = (arr[i]//place) % 10
        output_arr[count[digit]-1] = arr[i]
        count[digit] -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]
    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
RadixSort(arr)
print("Sorted array:", arr)