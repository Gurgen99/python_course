import math

def ex41(x,y,d):
    if d >= x**2 + y**2 - 1 and d <= x**2 + y**2 - 4:
        z = 0
    else:
        z = x + y
    return z
print(ex41(0, 0, 9))


def ex43(x,y,d):
    if d <= x**2 + y**2 -4 and d >= 3*x - 4*y:
        z = x**2 + 4
    else:
        z = 5*x
    return z
print(ex43(4,2,5))


def ex45(x,y,d):
    if d>= x-y and d<= x+y  and d<+ x**2 + y**2 - 1:
        z = 5*(x**2) + 2*y
    else:
        z = -7
    return z
print(ex45(1,3,6))


def ex47(x,y,d):
    if d>= x - y +1 and d<= x/2 + y +1:
        z = math.sin(x)
    else:
        z = 0 
    return z
print(ex47(5,6,9))


def ex49(x,y,d):
    if d>= x/2 - y + 1 and d<= x**2 - y:
        z = math.log(x**2 + 1)
    else:
        z = y+7 
    return z 
print(ex49(3,6,3))

