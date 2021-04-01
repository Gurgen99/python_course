import random

def generate_arr(n):
    arr = []
    for i in range(n):
        a = random.randint(-10,17)
        arr.append(a)
    return arr
a= generate_arr(4)
print(a)

def ex211(arr):
    s = 0 
    i = 0
    for a in arr:
        if a>0:
            s=s+a
            i+=1
    k = s/i
    return k
print(ex211(a))


def ex214(arr):
    s = 0
    i = 0
    for a in arr:
        if a<0:
            s= s+a
            i = i+1
    k = s/i
    return k
print(ex214(a))


def ex217(arr):
    s = 1
    for a in arr:
        if a%2 == 1:
            s = s * a**2
    return s
print(ex217(a))


def ex220(arr):
    dr = 0
    bc = 0
    for a in arr:
        if a>0:
            dr+=1
        else:
            bc+=1
    return dr, bc
print(ex220(a))


def ex223(arr):
    s = 0
    a = 1
    b = 10
    for c in arr:
        if c>a and c<b:
            s+=1
    return s
print(ex223(a))


def ex226(arr):
    s = 0
    t = 6
    for a in arr:
        if abs(a)<t:
            s+=1
    return s
print(ex226(a))


def ex229(arr):
    s = 1
    for a in arr:
        if a - arr[0]>0:
            s*=a
    return s
print(ex229(a))


def ex232(arr):
    s = 0
    for a in arr:
        if a%2 == 0:
            s+=1
    return s
print(ex232(a))


def ex235(arr):
    s = 1
    i = 0
    for a in arr:
        if a%2 == 1:
            s*= a**2
            i+=1
    k = s/i
    return k
print(ex235(a))


def ex238(arr):
    s = 0
    i = 0
    for a in arr:
        if a%3 == 0:
            s= s+a
            i+=1
    k = s/i
    return k
print(ex238(a)) 


def ex241(arr):
    s = 0
    k = 3
    for a in arr:
        if a%k == 0:
            s+=a
    return s
print(ex241(a))


def ex244(arr):
    s = 1
    for a in arr:
        if abs(a) % 5 == 2:
            s = s * a
    return s
print(ex244(a))


import math 
def ex247(arr):
    s = 0
    i = 0
    for a in arr:
        if a > arr[0]:
            s = s + (a**2)
            i+=1
    k = math.sqrt(s/i)
    return(k)
print(ex247(a))


def ex250(arr):
    s = 1
    for a in arr:
        if abs(a * arr[0]) == 2:
            s*=a
    return s
print(ex250(a))


def ex251(arr):
    for a in arr:
        if arr[0]> arr[1]:
            if arr[0]>arr[2]:
                if arr[0]>arr[3]:
                    max = arr[0]
                else:
                    max = arr[3]
            elif arr[2]>arr[3]:
                max = arr[3]
            else:
                max = arr[2]
        elif arr[1]>arr[2]:
            if arr[1]>arr[3]:
                max = arr[1]
            else:
                max = arr[3]
        elif arr[2]>arr[3]:
            max = arr[2]
        else:
            max = arr[3]
    return max
print(ex251(a))