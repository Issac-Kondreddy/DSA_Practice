a = [9,8,7,6,5,4,3,2,1]
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]

# print(a)


for i in range(len(a)):
    swap = False
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            swap = True
        if not swap:
            break

print(a)