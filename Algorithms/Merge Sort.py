def merge_sort(a):
    if len(a)<=1:
        return a
    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]
    left_arr = merge_sort(left)
    right_arr = merge_sort(right)
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    i, j = 0, 0
    merged = []
    while i< len(left_arr) and j < len(right_arr):
        if left_arr[i]<right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1
    merged.extend(left_arr[i:])
    merged.extend(right_arr[j:])
    return merged

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)  # merge_sort returns a sorted list
print(sorted_arr)  # Expected Output: [3, 9, 10, 27, 38, 43, 82]
