import random
def generate_arr(n):
    arr = []
    for i in range(n):
        a = random.randint(-10,10)
        arr.append(a)
    return arr


def ex311(x):
    y = []
    max = x[0]
    for a in x:
        if a > max:
            max = a
    for i in x:
        if i > 0:
            y.append(i+max)
    return y


def ex315(x,b):
    y = []
    for a in x:
        if a<b: 
            if a > 0:
                y.append(a)
        elif a < 0:
            y.append(a)
    return y







x = generate_arr(6)
print(x)
print(ex311(x))
print(ex315(x,6))

