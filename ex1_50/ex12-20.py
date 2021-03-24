import math

def ex12(a,x):
    if x>=-5 and x<=5:
        c = (1 + a**2) **6
    elif x>5:
        d = math.log(abs(x) **2)
        c= math.cos(d) + x**8
    else:
        c = a
    return c
print(ex12(5,7))



def ex14(a,b):
    if a+b<3:
        c = math.atan((a+b)**4)
    elif a+b>5:
        d= math.log10(a+b)
        c = d ** 2
    else:
        c = a**15
    return c
print(ex14(2,3))



def ex16(x,a):
    if abs(a)<3:
        c = math.sin(abs(x+a)**2) + math.cos((x**2)**2)
    else:
        d = (a**2 + x**2) **1/4
        c = d * math.log10(a**2 + x**4)
    return c
print(ex16(3,4))



def ex18(x,z):
    if x>=1 and x<=7:
        c = (abs(x) + 2*abs(z)) ** 1/4 + math.e ** abs(x+1)
    else:
        c = (math.log10((x+z)**7) ** 2)
    return c 
print(ex18(2,4))



def ex20(a,b,x):
    if a<3:
        d = math.cos(x+a+b)
        c = math.e ** d * math.log10(a + b**2)
    else:
        c = log10(4+ a**2 + b**2 )
    return c
print(ex20(2,3,4))