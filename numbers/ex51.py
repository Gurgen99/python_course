def ex51(a):
    b = a%10
    c = (a//10) % 10
    d = a//100
    if b == c+d:
        z = True
    else:
        z = False
    return z
print(ex51(164))


def ex53(a):
    b = a%10
    c = (a//10) % 10
    d = a//100
    k = b + c + d  
    if a > k:
        z = a/k
    else:
        z = b/a
    return z 
print(ex53(121))


def ex55(a):
    b = a%10
    c = (a//10) % 10
    d = a//100
    if b < c and b<d:
        mn = b
    elif c<b and c<d:
        mn = c
    else:
        mn = d
    return mn 
print(ex55(542))


def ex57(a):
    b = a%10
    c = (a//10) % 10
    d = a//100
    if a>300:
        z = c / d
    else:
        z = b / d
    return z 
print(ex57(131))


def ex59(a):
    b = a%10
    c = (a//10) % 10
    d = a//100
    if b > c:
        if b > d:
            mx = b
            if c > d:
                mj = c
                mn = d
            else:
                mj = d
                mn = c
        else:
            mx = d
            mj = b
            mn = c
    elif c > d:
        mx = c
        if b > d:
            mj = b
            mn = d
        else: 
            mj = d
            mn = b
    else :
         mx = d
         mj = c
         mn = b
    return mx, mj, mn
print(ex59(748))


def ex61(a):
    b = a%10
    c = (a//10)%10
    d = (a//100)%10
    e = a//1000
    if b+c == d+e:
        z = True
    else:
        z = False
    return z
print(ex61(1272))


def ex63(a):
    b = a%10
    c = (a//10)%10
    d = (a//100)%10
    e = a//1000
    if b==1 or c==1 or d==1 or e==1:
        z = 1
    else:
        z = 0
    return z
print(ex63(2345))


def ex65(a):
    b = a%10
    c = (a//10)%10
    if b*c ==12:
        z = "y=12"
    else:
        z = "y=0"
    return z
print(ex65(1284))


def ex67(a):
    b = a%10
    c = (a//10)%10
    d = (a//100)%10
    e = a//1000
    k = b + c + d + e  
    if a ==  k**2:
        z = "Yes"
    else:
        z = "No"
    return z
print(ex67(2312))


def ex69(a):
    b = a%10
    c = (a//10)%10
    d = (a//100)%10
    e = a//1000
    if b + c + d + e > 20:
        y = 1
    else:
        y = 0
    return y
print(ex69(8295))

