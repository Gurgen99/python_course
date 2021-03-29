import math


def ex71(x):
    while x >= 2.4 and x<=7.6:
        y = math.tan(2*x + x**2)  
        x = x + 0.2 
        print(x,y) 
ex71(3)


def ex73(x):
    while x>=7.5 and x<=12.5:
        y = (x+1)**2
        x+=0.2
        print(x,y)
ex73(8)



def ex75(x):
        while x>= -math.pi and x<= math.pi:
            y = math.sin(x)**2 + math.cos(x)
            x+=math.pi/8
            print(x,y)
ex75(-math.pi/2)



def ex77(x):
    while x >= -8 and x <= 8:
        if x>3:
            y = x**2 + 4*(x**8)
        else:
            y = 0
        x+=3
        print(x,y)
ex77(0)


def ex79(x):
    while x>=-4 and x<= 5:
        if x>1:
            y = math.log(x)
        else:
            y = -9
        x+=1
        print(x,y)
ex79(-3)


def ex81(x):
    while x>=-7.5 and x<=8.3:
        y = math.log(x**2 + 4)
        x+=0.3
        print(x,y)
ex81(-7)


def ex83(x):
    while x>=-4.8 and x<=5.2:
        y = math.atan(x+1)**2
        x+=0.2
        print(x,y)
ex83(-4)


def ex85(x):
    while x>=-3.3 and x<=2.7:
        y = abs(2*x + x**3)
        x+=0.3
        print(x,y)
ex85(-3.2)


def ex87(x):
    while x>=10 and x<=23:
        if x>7:
            y = math.e**math.sin(x)
        else:
            y = 0
        x+=3.2
        print(x,y)
ex87(11)


def ex89(x):
    while x>=-5 and x<=9:
        if x>3:
            y = math.log(x)
        else:
            y = -9
        x+=1.5
        print(x,y)
ex89(-3)



def ex91(n):
    i = 1
    x = 1
    s = 0
    while i>=1 and i<=n:
        y = x**2
        s= s+y
        x= x + 0.5 * abs(x-4)
        i = i + 1
    return s
print(ex91(30))


def ex94(n):
    i = 0
    x = -4.2
    s = 0
    while i>=0 and i<=n:
        y = x**2 - 2*x
        s+=y
        x+= 1 / math.tan(x)
        i+=1
    return s
print(ex94(20))


def ex97(n):
    i = 0
    x = 1 
    s = 1
    while i>=0 and i<=3*n:
        y = x
        s= s * y
        x += 0.5*x +7
        i+=1
    return s 
print(ex97(6)) 


def ex100(n):
    i = 0
    x = 1
    s = 1
    while i>= 0 and i<= n:
        y = x
        s*= y
        x+= 1 / math.tan(x) + 1
        i +=1
    return s
print(ex100(30))