import math


def generate(file_name):
    f = open(file_name, "r")
    arr = []
    for line in f.readlines():
        arr.append(int(line))
    f.close()
    return arr


def ex211(a):
    s = 0
    t = 0
    for i in range(len(a)):
        if a[i] > 0:
            s += a[i]
            t += 1
            k = s/t
    return k


def ex213(a):
    s = 0
    t = 0
    for i in range(len(a)):
        if a[i] < 0:
            s += a[i]**2
            t += 1
            k = math.sqrt(s/t)
    return k


def ex215(a):
    s = 0
    for i in range(len(a)):
        if i % 2 == 0:
            s += a[i]
    return s


def ex217(a):
    s = 0
    for i in range(len(a)):
        if i % 2 == 1:
            s += a[i]**2
    return s


def ex219(a):
    t = 0
    k = 4
    for i in range(len(a)):
        if i % k == 0 and i != 0:
            t += 1
    return t


a = generate("a.txt")
print(a)
print(ex211(a))
print(ex213(a))
print(ex215(a))
print(ex217(a))
print(ex219(a))
