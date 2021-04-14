import random
def generate_arr(n):
    arr = []
    for i in range(n):
        a = random.randint(-1,30)
        arr.append(a)
    return arr

def generate_matrix(n, m):
    matrix = []
    for i in range(n):
        matrix.append(generate_arr(m))
    return matrix


def ex452(matrix):
    b =[]
    for arr in matrix:
            k = (arr[0]**2) + (arr[-1]**2)
            b.append(k)
    return b


def ex453(a,b):
    y=[] 
    for arr in matrix:
        s=0
        for i in arr:
            if i>=a and i<=b:
                s+=i
        y.append(s)      
    return y


def ex454(matrix):
    b=[]
    for arr in matrix:
        s=0
        for i in arr:
            s+=i**2
        b.append(s)
    return b


def ex457(matrix):
    b = []
    for arr in matrix:
        s=0
        for i in arr:
            if i % 2 == 1:
                s+=i
        b.append(s)
    return b       


matrix = generate_matrix(3, 3)
for vec in matrix:
   print(vec)
print(ex452(matrix))
print(ex453(4,15))
print(ex454(matrix))
print(ex457(matrix))


