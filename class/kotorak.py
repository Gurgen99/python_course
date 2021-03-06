class Kotorak():
    def __init__(self,hamarich,haytarar):
       self.hamarich = hamarich
       self.haytarar =  haytarar 
    
    def __add__(self,other):
        tmp = Kotorak(0,0)
        if self.haytarar == other.haytarar:
            tmp.hamarich = self.hamarich + other.hamarich
            tmp.haytarar = self.haytarar
        else:
            tmp.haytarar = self.haytarar * other.haytarar
            tmp.hamarich = self.hamarich * other.haytarar + other.hamarich * self.haytarar
        return tmp

    def __sub__(self,other):
        tmp = Kotorak(0,0)
        if self.haytarar == other.haytarar:
            tmp.hamarich = self.hamarich - other.hamarich
            tmp.haytarar = self.haytarar
        else:
            tmp.haytarar = self.haytarar * other.haytarar
            tmp.hamarich = self.hamarich * other.haytarar - other.hamarich * self.haytarar
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
a = Kotorak(3,4)
b = Kotorak(2,5)
c = a + b
d = a - b
e = a * b 
f = a / b 
print(c.hamarich,c.haytarar)
print(d.hamarich,d.haytarar)
print(e.hamarich,e.haytarar)
print(f.hamarich,f.haytarar)