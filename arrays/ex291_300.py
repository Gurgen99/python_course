import random
def generate_arr(n):
    arr = []
    for i in range(n):
        a = random.randint(-10,10)
        arr.append(a)
    return arr


def ex291(x):
    y = []
    for a in x:
        if a < 0:
            y.append(a)
    return y


def ex293(x):
    a = -1
    b = 5
    y = []
    for i in x:
        if i<-1 or i>5:
            y.append(i)
    return y


def ex295(x):
    y = []
    for i in range(len(x)):
        if i % 2 ==1:
            y.append(x[i])
    return y


def ex297(x):
    k = 5
    y = []
    for a in x:
        if a < k:
            y.append(a)
    return y


def ex299(x):
    y = []
    for a in x:
        if a % 2 ==0:
            y.append(a)
    return y


x = generate_arr(6)
print(x)
print(ex291(x))
print(ex293(x))
print(ex295(x))
print(ex297(x))
print(ex299(x))