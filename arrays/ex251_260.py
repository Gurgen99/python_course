import random
def generate_arr(n):
    arr=[]
    for i in range(n):
        a = random.randint(-10,10)
        arr.append(a)
    return arr


def ex253(arr):
    max = arr[0]
    min = arr[0]
    for a in arr:
        if a>max:
            max = a
        if a<min:
            min = a   
    return max, min


def ex256(arr):
    min = arr[0]
    s = 0
    for i in range(len(arr)):
        if arr[i]<min:
            min = arr[i]
            ind = i
    s= min+ ind
    return s


def ex257(arr):
    max = arr[0]
    for a in arr:
        if max<a:
            max = a
    return max


a = generate_arr(8)
print(a)
print(ex253(a))
print(ex256(a))
print(ex257(a))