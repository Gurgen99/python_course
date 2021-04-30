import random
import math


class Array():
    def __init__(self, n):
        self.n = n
        self.arr = self.generate_arr()

    def generate_arr(self):
        arr = []
        n = self.n
        for i in range(n):
            a = random.randint(10, 100)
            arr.append(a)
        return arr

    def ex231(self):
        s = 0
        n = self.arr
        for i in range(len(n)):
            # print(n)
            if n[i] % 2 == 0:
                s += n[i]**2
        return s

    def ex233(self):
        s = 1
        t = 0
        k = self.arr
        for i in range(len(k)):
            # print(k)
            if k[i] % 2 == 0:
                s *= k[i]
                t += k[i]
        return s, t

    def ex234(self):
        s = 0
        t = 0
        n = self.arr
        for i in range(len(n)):
            # print(n)
            if n[i] % 2 == 1:
                s += n[i]**2
                t += 1
                l = math.sqrt(s/t)
        return l

    def ex236(self):
        s = 1
        t = 0
        k = self.arr
        for i in range(len(k)):
            if k[i] % 2 == 1:
                s *= k[i]
                t += 1
        return s, t

    def ex242(self, m):
        s = 1
        arr = self.arr
        for i in range(len(arr)):
            # print(arr)
            if arr[i] % m == 0:
                s *= arr[i]
        return s

    def ex245(self):
        s = 0
        n = self.arr
        for i in range(len(n)):
            if (n[i] + i) % 3 == 0:
                s += n[i]**2
        return s

    def ex246(self):
        m = 0
        n = 0
        arr = self.arr
        for i in range(len(arr)):
            k = math.sqrt(arr[i])
            if int(k) == k:
                print(k)
                m += arr[i]
                n += 1
                q = m/n
        return q

    def ex248(self, k):
        s = 0
        arr = self.arr
        for i in range(len(arr)):
            # print(arr)
            if (arr[i]+i) ** 2 % k == 0:
                s += arr[i]
        return s

    def ex249(self, k):
        s = 1
        n = self.arr
        for i in range(len(n)):
            if abs(n[i]-i) > k:
                s *= n[i]**2
        return s
    
    def ex256(self):
        s = 0
        arr = self.arr
        mn = arr[0]
        for i in range(len(arr)):
            # print(arr)
            if arr[i] < mn:
                mn = arr[i]
                k = i
        s = mn +k
        return s


a = Array(5)
print(a.generate_arr())
print(a.ex231())
print(a.ex233())
print(a.ex234())
print(a.ex236())
print(a.ex242(5))
print(a.ex245())
# print(a.ex246())
print(a.ex248(5))
print(a.ex249(70))
print(a.ex256())