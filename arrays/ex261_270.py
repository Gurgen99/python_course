import random
def generate_arr(n):
    arr = []
    for i in range(n):
        a = random.randint(-10,10)
        arr.append(a)
    return arr


def ex261(x,y):
    s = 0
    i = 0
    for a in x:
        s = s+a
        i+=1
    for b in y:
        s+=b
        i+=1
    k =s/i
    return k


def ex263(x,y):
    i = 0
    for a in x:
        if a>0:
            i+=1
    for b in y:
        if b >0:
            i+=1
    return i


def ex265(x,y):
    s = 0
    i = 1
    for a in x:
        s+=a
    for b in y:
        if b != 0:
            i=i*b
    g = s/i
    return g


def ex267(x,y):
    t = 7
    s = 0 
    for a in x:
        if a%t == 0:
            s+=a
    for b in y:
        if b%t == 0:
            s+=b
    return s


def ex269(x,y):
    s = 0
    for i in range(len(x)):
        if i % 2 == 0 and i != 0:
            s+= x[i]
    for j in range(len(y)):
        if j % 2 == 1:
            s+= y[j]
    return s
            

x = generate_arr(4)
y = generate_arr(4)
print(x)
print(y)
print(ex261(x,y))
print(ex263(x,y))
print(ex265(x,y))
print(ex267(x,y))
print(ex269(x,y))