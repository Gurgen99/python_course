class Kotorak():
    def __init__(self,hamarich,haytarar):
       self.hamarich = hamarich
       self.haytarar =  haytarar 
    
    def __add__(self,other):
        tmp = Kotorak(0,0)
        tmp.hamarich = self.hamarich + other.hamarich
        tmp.haytarar = self.haytarar + other.haytarar
        return tmp

    def __sub__(self,other):
        tmp = Kotorak(0,0)
        tmp.hamarich = self.hamarich - other.hamarich
        tmp.haytarar = self.haytarar - other.haytarar
        return tmp

    def __mul__(self,other):
        tmp = Kotorak(1,1)
        tmp.hamarich = self.hamarich * other.hamarich
        tmp.haytarar = self.haytarar * other.haytarar
        return tmp
    
    def __truediv__(self,other):
        tmp = Kotorak(1,1)
        tmp.hamarich = self.hamarich / other.hamarich
        tmp.haytarar = self.haytarar / other.haytarar
        return tmp
a = Kotorak(10,20)
b = Kotorak(5,10)
c = a + b
d = a - b
e = a * b 
f = a / b 
print(f.hamarich,f.haytarar)