a = 8
b = 7
c = 9
if a>=b and a>=c:
     d = (a-b)*c
     print(d)
else:
     if b>=c:
          d = (b-a)*c
          print(d)
     else:
         d= (c-a)*b
         print(d)
