def euclidean(a,b):
    if b==0:
        return a
    return euclidean(b, a%b)

print(euclidean(48, 24))
print(euclidean(48, 18))
print(euclidean(98, 94))
print(euclidean(96, 33))


def gcd1(a, b):
    while a!=b:
        if a >b:
            a = a - b
        else:
            b = b - a
    return a

print(gcd1(48, 24))
print(gcd1(48, 18))
print(gcd1(98, 94))
print(gcd1(96, 33))