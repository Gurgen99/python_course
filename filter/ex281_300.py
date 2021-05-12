import random
def generate_arr(n):
    arr = []
    for i in range(n):
        a = random.randint(-20,20)
        arr.append(a)
    return arr
a = generate_arr(6)


ex282 = list(filter(lambda a: a!=0, a))


def ex284(b,c):
    k = list(filter(lambda a: b<=a<=c, a))
    return k 

ex286 = list(filter(lambda a: a%2==0, a))

def ex288(a):
    y = []
    for i in range(len(a)):
        if i%2==1:
            y.append(a[i])
    return y

ex290 = list(filter(lambda x: x%6==1 and x!=1, a))    

ex292 = list(filter(lambda y: y%7!=0, a))

def ex294(a):
    y = []
    for i in range(len(a)):
        if i%2!=1:
            y.append(a[i])
    return y

def ex296(k):
    k = list(filter(lambda x: x%k!=2, a))
    return k

ex298 = list(filter(lambda a: a%2!=0, a)) 

def ex300(k):
    z = list(filter(lambda x: x**2 > k, a))
    return z

print(a)
print(ex282)
print(ex284(-10,10))
print(ex286
print(ex288(a))
print(ex290)
print(ex292)
print(ex294(a))
print(ex296(5))
print(ex298)
print(ex300(10))