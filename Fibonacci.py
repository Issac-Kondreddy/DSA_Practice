#using a loop
# prev0 = 0
# prev1 = 1
# print(prev0)
# print(prev1)
# for fibo in range(18):
#     newfibo = prev0 + prev1
#     print(newfibo, end = " ")
#     prev0 = prev1
#     prev1 = newfibo


#using a recursion
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(20))