import math

def ex41(x,y):
    if x**2 + y**2 >= 1 and  x**2 + y**2 <=4:
        z = 0
    else:
        z = x + y
    return z
print(ex41(0, 1)) 

def ex43(x,y):
    if x**2 + y**2 <=4 and y<= 3*x / 4:
        z = x**2 + 4
    else: 
        z = 5*x 
    return z 
print(ex43(1,2))

 
def ex45(x,y):
    if  y>= -x and y>=x  and x**2 + y**2 <= 1:
        z = 5*(x**2) + 2*y
    else:
        z = -7
    return z
print(ex45(1,3))


def ex47(x,y):
    if y<= x+1 and y<= -x/2 + 1 and y>=0:
        z = math.sin(x)
    else:
        z = 0 
    return z
print(ex47(5,3)) 


def ex49(x,y):
    if y<= x/2 + 1 and y<= x**2  and  y>=0:
        z = math.log(x**2 + 1)
    else:
        z = y+7 
    return z 
print(ex49(4,2)) 

