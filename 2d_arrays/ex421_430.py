import math
import random
def generate_arr(n):
    arr = []
    for i in range(n):
        a = random.randint(1,30)
        arr.append(a)
    return arr

def generate_matrix(n, m):
    matrix = []
    for i in range(n):
        matrix.append(generate_arr(m))
    return matrix


def ex421(k):
    y = []
    for i in range(1,len(matrix)):
        for j in range(0,i):
            if matrix[i][j] % k ==0:
                y.append(matrix[i][j])
    return y


def ex423(matrix):
    s = 0
    t = 0
    for i in range(len(matrix)):
        for j in range(i+1):
            if matrix[i][j] % 2 ==0:
                t += 1
                s = matrix[i][j] **2 
                p = math.sqrt (s/t)
    return p


def ex425(matrix):
    t = 0
    for i in range(len(matrix)):
        for j in range(0,i):
            if matrix[i][j] % 2 == 0:
                t+= 1
    return t


def ex427(k):
    s = 1
    for i in range(len(matrix)):
        for j in range(len(matrix)-i):
            if matrix[i][j] % k == 0:
                s*= matrix[i][j] 
    return s


def ex429(matrix):
    k = 5
    t = 0
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[i][j] % k == 2:
                t+=1
    return t



matrix = generate_matrix(5, 5)
for vec in matrix:
   print(vec)
print(ex421(2))
print(ex423(matrix))
print(ex425(matrix))
print(ex427(3))
print(ex429(matrix))