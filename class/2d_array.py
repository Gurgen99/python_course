import random
import math


class Matrix():
    def __init__(self, n,m):
        self.n = n
        self.m = m
        self.matrix = self.generate_matrix()

    def generate_arr(self):
        arr = []
        for i in range(self.m):
            a = random.randint(-10, 30)
            arr.append(a)
        return arr

    def generate_matrix(self):
        matrix = []
        for i in range(self.n):
            matrix.append(self.generate_arr())
        return matrix
        

    def ex422(self):
        s = 0 
        t = 0
        for i in range(1,len(self.matrix)):
            for j in range(0,i):
                if  self.matrix[i][j] % 5 == 0:
                    s+=self.matrix[i][j]
                    t+=1        
        return s/t

    def ex424(self):
        s = 0
        t = 0
        for i in range(len(self.matrix)):
            for j in range(i+1):
                if self.matrix[i][j] % 2 == 1:
                    s+= self.matrix[i][j]
                    t+= 1
        return s/t

    def ex426(self):
        s = 0
        for i in range(len(self.matrix)-1):
            for j in range(len(self.matrix)-1-i):
                if self.matrix[i][j] % 2 == 0:
                    s+= self.matrix[i][j]
        return s

    def ex428(self):
        t = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)-1):
                if self.matrix[i][j] == 0:
                    t+=1
        return t
    
    def ex430(self):
        s = 0
        t = 0
        for i in range(len(self.matrix)):
            for j in range(i+1):
                if self.matrix[i][j] % 2 ==0:
                    s+=self.matrix[i][j]
                    t+=1
                    k= s / t
        return k

    def ex432(self):
        s = 0
        t = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)-1):
                if (i + j) % 2 == 1:
                    s+=self.matrix[i][j] ** 2
                    t+=1
                    k = math.sqrt(s/t)
        return k

    def ex434(self):
        s = 0
        for i in range(len(self.matrix)):
            for j in range(i+1):
                if abs(self.matrix[i][j]) >= 5.4 and abs(self.matrix[i][j]) <= 15.3:
                    s+=self.matrix[i][j]
        return s

    def ex436(self,a,b):
        s = 0
        t = 0
        for i in range(1,len(self.matrix)):
            for j in range(0,i):
                if self.matrix[i][j] >= a and self.matrix[i][j]<=b:
                    s+= self.matrix[i][j]
                    t+=1
                    k =s/t
        return k
    
    def ex438(self):
        t = 0
        for i in range(1,len(self.matrix)):
            for j in range(i+1):
                if self.matrix[i][j] > 0 and i % 2 == 0:
                    t+=1 
        return t

    def ex440(self):
        s = 0
        for i in range(len(self.matrix)):
            for j in range(i+1,len(self.matrix)):
                if (i + j) % 2 == 0:
                    s+=self.matrix[i][j]
        return s
    def ex442(self):
        s = 0
        t = 0
        for i in range(len(self.matrix)-1):
            for j in range(len(self.matrix)-1-i):
                if self.matrix[i][j] < 0:
                    s+=self.matrix[i][j]
                    t+= 1
        return s/t

    def ex444(self):
        t = 0
        for i in range(len(self.matrix)):
            for j in range(i+1,len(self.matrix)):
                if self.matrix[i][j] < 0 and j % 2 == 1:
                    t+=1
        return t
    
    def ex446(self,a,b):
        s = 0 
        for i in range(len(self.matrix)):
            for j in range(i,len(self.matrix)):
                if  self.matrix[i][j] >= a and self.matrix[i][j] <= b:
                    s+= self.matrix[i][j]
        return s

    def ex448(self):
        s = 0
        t = 0
        for i in range(len(self.matrix)):
            for j in range(i,len(self.matrix)):
                if (i + j) % 2 ==0:
                    s+= self.matrix[i][j]
                    t+=1
        return s/t 

    def ex450(self):
        s = 0
        for i  in range(1,len(self.matrix)):
            for j in range(len(self.matrix)-i, len(self.matrix)):
                b = self.matrix[i][j] % 1
                s+=b
        return s 


a = Matrix(4,4)
print(a.matrix)
print(a.ex422())
print(a.ex424())
print(a.ex426())
print(a.ex428())
print(a.ex430())
print(a.ex432())
print(a.ex434())
print(a.ex436(3,20))
print(a.ex438())
print(a.ex440())
print(a.ex442())
print(a.ex444())
print(a.ex446(5,15))
print(a.ex448())
print(a.ex450())