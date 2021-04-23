def generate(file_name):
    f = open(file_name, "r")
    st = ""
    for line in f.readlines():
        st += line
    f.close()
    return st


def generate_2(file_name):
    f = open(file_name, "r")
    lines = f.readlines()
    st1 = lines[0]
    st2 = lines[1]
    f.close()
    return st1, st2


def ex646(a):
    t = 0
    for i in range(len(a)):
        if a[i] == "a":
            t += 1
    return t


def ex648(a):
    t = 0
    for i in range(len(a)):
        if a[i] == "x":
            for j in range(i, len(a)):
                if a[j] == "0":
                    t += 1
    return t


def ex650(b, c):
    t = 0
    for i in range(len(b)):
        if b[i] in c:
            t += 1
    return t


def ex654(a):
    k = ""
    for i in range(len(a)):
        if a[i] != "a":
            k += a[i]
    return k


def ex656(a):
    k = ""
    k = a.replace("x", "yy")
    return k


a = generate("b.txt")
b, c = generate_2("b.txt")
print(a)
print(b, c)
print(ex646(a))
print(ex648(a))
print(ex650(b, c))
print(ex654(a))
print(ex656(a))
