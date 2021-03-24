def ex21(a,b,c,d,e,f):
    k = max(a,b,c,d,e,f)
    m = min(a,b,c,d,e,f)
    return k, m
print(ex21(3,4,5,7,8,9))



def ex23(a,b,c,d,e,f,g):
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1:
        n = "true"
    else:
        n = "false"
    return n
print(ex23(2,3,4,5,6,7,1))


def ex24(a,b,c):
    if (a==2 and b==2 ) or a==2 and c==2 or b==2 and c==2:
        n = "true"
    else:
        n = "false"
    return n
print(ex24(1,4,5))


def ex25(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        y = 1
    else:
        y = 2
    return y
print("y=" ,ex25(6,6,7))


def ex26(a,b,c):
    if a%2 == 0 or b%2 == 0 or c%2 == 0:
        k = 1 
    else:
        k = 2
    return k
print(ex26(3,5,8))


def ex27(a,b,c):
    if  b-a == c-b:
        k = "true"
    else:
        k = 'false'
    return k
print(ex27(2,4,6))


def ex28(a,b,c):
    if b/a == c/b:
        k = 'true'
    else:
        k = "false"
    return k
print(ex28(3,6,12))


def ex30(a,b,c):
    if a>b:
        if a>c:
            mx = a
            if b>c:
                mj = b
                mn = c
            else:
                mj = c
                mn = b
        else:
            mx = c
            mj = a
            mn = b
    elif b>c:
        mx = b
        if a>c:
            mj = a
            mn = c
        else:
            mj = c
            mn = a
    else:
        mx = c
        mj = b
        mn = a
    return mx, mj, mn
print(ex30(7,45,6))
        
        
