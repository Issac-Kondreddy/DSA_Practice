def insertionsort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j>=0 and a[j]>key:
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = key
    return a

a = [65,22,34,1,12,11]
print(insertionsort(a))