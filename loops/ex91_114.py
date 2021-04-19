import math

def ex92(n):
    i = 1
    s = 1 
    x = 0.5
    while i>=1 and i<=n:
        y = x
        s*=y
        x = math.tan(x+2)
        i+=1
    return s

def ex93(n):
    i = 5 
    s = 1
    x = 0.5
    while i>=5 and i<=n:
        y = x**2 + x
        s*=y
        x = math.log10(x+2)
        i+=1
    return s

def ex95(n):
    i = 0 
    x = 1
    s = 0
    while i >= 0 and i<=n:
        y = x**2 - x
        s+=y
        x=math.sin(x)**2
        i+=1
    return s

def ex96(n):
    i = 1
    x = 22
    s = 0
    while i>=1 and i<=n:
        y = x**2
        s+=y
        x = x-3.4
        i+=1
    return s


def ex98(n):
    i = n
    x = 1
    s = 0
    while i>=n and x<=2*n:
        y = x
        s+= y
        x = 3.4 * abs(x-7)
        i+=1
    return s

def ex99(n):
    i = 1
    x = 5
    s = 0
    while i>=1 and i<=n:
        y = x**2
        s+= y
        x = x**2 + 7
        i+=1
    return s

def ex101(n):
    i = 1
    s = 0
    x = 1
    y = 2
    while i>=1 and i<=n:
        z = (x+y)**2 
        s += z
        x = 2*abs(x+3)
        y = y**2 - 4
        i+=1
    return s

def ex103(n):
    i = 4
    x = 2
    y = 1
    s = 1
    while i>=4 and i<=n:
        z = x**2 + y 
        s+=z
        x = x**2
        y = math.tan(y)
        i+=1
    return s

def ex105(n):
    i = 0
    x = 1
    y = 1
    s = 0
    while i>=0 and i<=n:
        z = x**2 + y
        s+=z
        x = math.sin(x) + 3
        y = math.cos(y)
        i+=1
    return s

def ex107(n):
    i = 0
    x = 1
    y = 1
    s = 1
    while i>=0 and i<=n:
        z = math.cos(x+y)
        s*=z
        x = x/2
        y = y/3
        i+=1
    return s

def ex109(n):
    i = 1
    a = 1 
    b = 2 
    s = 0
    while i>=1 and i<=n:
        z = a + b**2
        s+=z
        a = 6*a - 4
        b = 5*math.log(b) +3
        i+=1
    return s

def ex111(n,x):
    s = x
    for i in range(n):
        s = s + x**(4*i +1) / 4*i+1
    return s 

def ex113(n,x):
    s = x-1 / x**2+1
    for i in range(n):
        s = s + (1/ 2*i+1) * s**(2*i+1)
    return s


print(ex92(5))
print(ex93(4))
print(ex95(5))
print(ex96(8))
print(ex98(4))
print(ex99(5))
print(ex101(5))
print(ex103(4))
print(ex105(4))
print(ex107(8))
print(ex109(6))
print(ex111(6,4))
print(ex113(4,5))