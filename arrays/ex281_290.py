import random
def generate_arr(n):
    arr = []
    for i in range(n):
        a = random.randint(-10,10)
        arr.append(a)
    return arr


def ex281(x):
    y = []
    for a in x:
        if a > 0:
            y.append(a)
    return y


def ex283(x):
    y = []
    for a in x:
        if a % 2 ==1:
            y.append(a)
    return y


def ex285(x):
    y = []
    p = 2
    for a in x:
        if a % p == 0 and a != 0:
            y.append(a)
    return y


def ex287(x):
    y = []
    for i in range(len(x)):
        if i != x[i]:
            y.append(x[i])
    return y


def ex289(x):
    y = []
    c = 3
    d = 20
    for a in x:
        if a**2 > c and a**2 < d:
            y.append(a)
    return y


x = generate_arr(5)
print(x)
print(ex281(x))
print(ex283(x))
print(ex285(x))
print(ex287(x))
print(ex289(x))