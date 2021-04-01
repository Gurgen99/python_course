import math
import random


def generate_arr(n):
    arr = []
    for i in range(n):
        a = random.randint(-10, 17)
        arr.append(a)
    return arr


def ex211(arr):
    s = 0
    i = 0
    for a in arr:
        if a > 0:
            s = s+a
            i += 1
    k = s/i
    return k


def ex214(arr):
    s = 0
    i = 0
    for a in arr:
        if a < 0:
            s = s+a
            i = i+1
    k = s/i
    return k


def ex217(arr):
    s = 1
    for a in arr:
        if a % 2 == 1:
            s = s * a**2
    return s


def ex220(arr):
    dr = 0
    bc = 0
    for a in arr:
        if a > 0:
            dr += 1
        else:
            bc += 1
    return dr, bc


def ex223(arr):
    s = 0
    a = 1
    b = 10
    for c in arr:
        if c > a and c < b:
            s += 1
    return s


def ex226(arr):
    s = 0
    t = 6
    for a in arr:
        if abs(a) < t:
            s += 1
    return s


def ex229(arr):
    s = 1
    for a in arr:
        if a - arr[0] > 0:
            s *= a
    return s


def ex232(arr):
    s = 0
    for a in arr:
        if a % 2 == 0:
            s += 1
    return s


def ex235(arr):
    s = 1
    i = 0
    for a in arr:
        if a % 2 == 1:
            s *= a**2
            i += 1
    k = s/i
    return k


def ex238(arr):
    s = 0
    i = 0
    for a in arr:
        if a % 3 == 0:
            s = s+a
            i += 1
    k = s/i
    return k


def ex241(arr):
    s = 0
    k = 3
    for a in arr:
        if a % k == 0:
            s += a
    return s


def ex244(arr):
    s = 1
    for a in arr:
        if abs(a) % 5 == 2:
            s = s * a
    return s


def ex247(arr):
    s = 0
    i = 0
    for a in arr:
        if a > arr[0]:
            s = s + (a**2)
            i += 1
    k = math.sqrt(s/i)
    return(k)


def ex250(arr):
    s = 1
    for a in arr:
        if abs(a * arr[0]) == 2:
            s *= a
    return s


a = generate_arr(4)
print(a)
print(ex211(a))
print(ex214(a))
print(ex217(a))
print(ex220(a))
print(ex223(a))
print(ex226(a))
print(ex229(a))
print(ex232(a))
print(ex235(a))
print(ex238(a))
print(ex241(a))
print(ex244(a))
print(ex247(a))
print(ex250(a))
