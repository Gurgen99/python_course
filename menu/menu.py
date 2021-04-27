l = open("cucak","r")
k = []
for line in l.readlines():
    k.append(line)
l.close()
f = open("cucak", "w")
tvyalner = ("""Mutqagreq 1, ete uzum eq avelacnel apranq
Mutqagreq 2, ete uzum eq tesnel bolor apraqner@
Mutqagreq 3, ete uzum eq jnjel apranq@
mutqagreq 4, ete uzum eq durs gal""")

while True:
    print(tvyalner)
    a = (input("Mutqagrel:"))
    if a == "1":
        b = input("Greq apranqi anun:")
        k.append(b)
        # print(k)
    elif a == "2":
        print(k)
    elif a == "3":
        c = input("Greq apranqi anuny:") 
        t = k.index(c)
        k.pop(t)
    elif a == "4":
        break
    else:
        print("Sxal mutqagrum!")
    # f.write("Dzer karciqy:")
    # f.write(input("Dzer karciqy:"))
    # break
f.write(str(k))
f.write("\n")
f.close()

 