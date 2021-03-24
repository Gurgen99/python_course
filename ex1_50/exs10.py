a = 4
b = 10
c = 2.5
d = 10.8
if a >= b and a >= c and a >= d:
    print("a", type(a))
else:
    if b >= c and b >= d:
        print("b", type(b))
    else:
        if c >= d:
            print("c", type(c))
        else:
            print("d", type(d))

    