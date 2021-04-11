import random
def ex301(k):
    x = []
    for i in range(10,100):
        if i % k == 0:
            x.append(i)
    return x


def ex304(n):
    x = []
    for a in range(10,100):
        if a % n == 2:
            x.append(a)
    return x

 
print(ex301(7))
print(ex304(8))