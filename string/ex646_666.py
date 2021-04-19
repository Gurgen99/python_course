import random


def generate_str(n):
    s = ""
    for i in range(n):
        k = random.randint(97, 122)
        s += chr(k)
    return s


def ex646(s1):
    t = 0
    for i in range(len(s1)):
        if s1[i] == "a":
            t += 1
    return t


def ex648(s):
    t = 0
    for i in range(len(s)):
        if s[i] == "x":
            k = i
    for j in range(k, len(s)):
        if s[j] == "0":
            t += 1
    return t


def ex650(s1, s2):
    t = 0
    for i in range(len(s1)):
        if s1[i] in s2:
            t += 1
    return t


def ex652(s1, s2):
    s = ""
    for i in range(len(s2)):
        if s2[i] in s1:
            s += s2[i]
    return s


def ex654(s1):
    k = ""
    k = s1.replace("a", "")
    return k


def ex656(s1):
    k = ""
    k = s1.replace("x", "yy")
    return k


def ex657(s1):
    k = ""
    for i in range(0, len(s1), 2):
        if s1[i] >= s1[i+1]:
            k += s1[i]
        else:
            k += s1[i+1]
    return k


def ex660(s1):
    k = ""
    for i in range(len(s1)):
        if i % 2 == 0 or i == 0:
            k += s1[i]
        else:
            k += "a"
    return k


def ex664(v):
    a = 0
    b = 0
    k = False
    for i in range(len(v)):
        if v[i] == "c":
            a += 1
        elif v[i] == "d":
            b += 1
        if v[i] > "c":
            k = True
    if k == True:
        return a
    else:
        return b 
    


def ex666(t):
    mj = len(t)//2 
    return t[:mj-1] + t[mj+2:] 



s1 = generate_str(14)
s2 = generate_str(14)
s3 = generate_str(11)
print(s1)
print(s2)
print(ex646(s1))
s = "ahsakx02000000"
print(s, "  ", ex648(s))
print(ex650(s1, s2))
print(ex652(s1, s2))
print(ex654(s1))
print(ex656(s1))
print(ex657(s1))
print(ex660(s1))
v = "abababab"
print(ex664(v))
print(ex666(s3), "   " ,s3)