import random
def ex301(n):
    x = []
    k = 5 
    for i in range(n):
        if i % k == 0 and i>9:
            x.append(i)
    return x


def ex304(arr):
    x = []
    n = 5
    for a in range(arr):
        if a % n == 2 and a > n:
            x.append(a)
    return x

 
print(ex301(99))
print(ex304(100))