import sys
tiv1 = sys.argv[1]
nshan = sys.argv[2]
tiv2 = sys.argv[3]
a = int(tiv1)
b = int(tiv2)
if nshan == "+":
    c = a + b
elif nshan == "*":
    c = a * b
elif nshan == "-":
    c = a - b 
elif nshan == "/":
    c = a / b
else:
    print("Sxal nshan")
    sys.exit(0)
print(c)