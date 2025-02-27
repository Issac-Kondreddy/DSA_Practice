a = [9,8,7,6,5,4,3,2,1]

def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if a[j]< a[min_index]:
                min_index = j
        if min_index != i:
            a[i],a[min_index] = a[min_index],a[i]
    return a

print(selection_sort(a))
