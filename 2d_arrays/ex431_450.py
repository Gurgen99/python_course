import math
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


def ex431(matrix):
    t = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)-i-1,len(matrix)):
            if (i+j) % 2 == 1:
                t += 1
    return t 


def ex433(a,b):
    t = 0
    for i in range(len(matrix)-1):
        for j in range(len(matrix)-1-i):
                if matrix[i][j]>=a and matrix[i][j]<=b:
                        t+=1
    return t


def ex435(matrix):
    t = 0
    for i in range(len(matrix)-1):
        for j in range(len(matrix)-1-i):
            if int(matrix[i][j]) % 5 == 0:
                t+=1
    return t


def ex437(matrix):
    s = 0
    t = 0
    for i in range(1,len(matrix)):
        for j in range(0,i):
            if matrix[i][j]==int(matrix[i][j]):
                s+= matrix[i][j]**2
                t+=1
                k = math.sqrt(s/t)
    return k


def ex439(matrix):
    s = 1
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            if (i+j) % 2 ==1:
                s*=matrix[i][j]
    return s


def ex441(matrix):
    s = 0
    t = 0
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            if matrix[i][j] > 0:
                s+= matrix[i][j]**2
                t+= 1
                k = math.sqrt(s/t)
    return k


def ex443(matrix):
    t = 0
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            if matrix[i][j]==0:
                t+=1
    return t


def ex445(k):
    t = 0
    for i in range(1,len(matrix)):
        for j in range(0,i):
            if abs(matrix[i][j]) > k:
                t+=1
    return t


def ex447(a):
    s = 1
    for i in range(len(matrix)):
        for j in range(len(matrix)-i-1,len(matrix)):
            if matrix[i][j] < a:
                s*=matrix[i][j]
    return s


def ex449(matrix):
    s = 0
    for i in range(len(matrix)-1):
        for j in range(len(matrix)-1-i):
            if int(matrix[i][j]) % 4 == 0:
                s+=matrix[i][j]
    return s 


matrix = generate_matrix(6, 6)
for vec in matrix:
   print(vec)
print(ex431(matrix))
print(ex433(0,15))
print(ex435(matrix))
print(ex437(matrix))
print(ex439(matrix))
print(ex441(matrix))
print(ex443(matrix))
print(ex445(7))
print(ex447(17))
print(ex449(matrix))