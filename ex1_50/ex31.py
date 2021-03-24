def ex31(a,b,c,d):
    if a>b and a>c and a>d:
        mx = a
    elif b>a and b>c and a>d:
        mx = b
    elif c>a and c>b and c>d:
        mx = c
    else:
        mx = d
    return(mx)
print(ex31(3,6,8,4))


def ex34(a,b,c,d):
    if a+b == c+d:
        k = "true"
    elif a+c == b+d:
        k = "true"
    elif a+d == b+c:
        k = "true"
    else:
        k = "false"
    return k
print(ex34(1,2,3,9))


def ex36(a,b,c,d):
    e = 0
    if a%2 ==1:
        e = e+1
    if b%2 == 1:
        e= e+1
    if c%2==1:
        e= e+1
    if d%2=1:
        e = e+1
    if e>=2:
        k = 1
    else:
        k = 2
    return k 
print(ex36(2,3,5,6))



