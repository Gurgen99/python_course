import math
class Shape():
    def __init__(self):
        pass

    def draw_me(self):
        raise NotImplementedError


class D_2(Shape):

    def draw_my(self):
        pass

    def space(self):
        raise NotImplementedError


class D_3(Shape):
    def draw_me(self):
        pass

    def volume(self):
        raise NotImplementedError


class Squure(D_2):
    def __init__(self, a):
        self.a = a

    def draw_me(self):
        print("I'm a squure")

    def space(self):
        s = self.a ** 2
        return s


class Triangle(D_2):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def draw_me(self):
        print("I'm a triangle")

    def space(self):
        s = self.a * self.h / 2
        return s


class Rectangular(D_2):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw_me(self):
        print("i'm a rectangular")

    def space(self):
        s = self.a * self.b
        return s

class Cone(D_3):
    def __init__(self,r,h):
        self.r = r
        self.h = h
    def draw_me(self):
        print("I'm a cone")
    def volume(self):
        s = (math.pi * (self.r**2) * self.h) / 3
        return s

class Cube(D_3):
    def __init__(self,a):
        self.a = a
    def draw_me(self):
        print("I'm a cube")
    def volume(self):
        s = self.a**3
        return s

class Cylinder(D_3):
    def __init__(self,r,h):
        self.r = r
        self.h = h
    def draw_me(self):
        print("I'm acylinder")
    def volume(self):
        s = math.pi * self.r**2 * self.h 
        return s




k1 = Squure(4)
print(k1.draw_me())
print(k1.space())

k2 = Triangle(6, 7)
print(k2.draw_me())
print(k2.space())

k3 = Rectangular(8, 4)
print(k3.draw_me())
print(k3.space())

q1 = Cone(5,8)
print(q1.draw_me())
print(q1.volume())

q2 = Cube(5)
print(q2.draw_me())
print(q2.volume())

q3 = Cylinder(2,4)
print(q3.draw_me())
print(q3.volume())