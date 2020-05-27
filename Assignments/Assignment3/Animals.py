class Elephant:
    def __init__(self, color = "", legs = 0):
        self.__color = color					#Encapsultion
        self.__legs = legs
    def get_color(self):
        return (self.color)
    def get_legs(self):
        return  (self.legs)
    def set_color(self, c):
        self.color = c
    def set_legs(self, l):
        self.legs = l
class Dog:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

class Cat:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l
class Rabbit:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

class Tiger:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l
class Lion:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

class Penguin:
    def __init__(self, color = "", legs = 0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

class Dolphin:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

class Monkey:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

class Giraffe:
    def __init__(self, color="", legs=0):
        self.__color = color
        self.__legs = legs

    def get_color(self):
        return (self.color)

    def get_legs(self):
        return (self.legs)

    def set_color(self, c):
        self.color = c

    def set_legs(self, l):
        self.legs = l

elephant = Elephant()
elephant.set_color("grey")
elephant.set_legs(4)
print("Elephant has", elephant.get_color(), "color and", elephant.get_legs(), "legs")

d = Dog()
d.set_color("Yellow")
d.set_legs(4)
print("This dog has",d.get_color(), "color and", d.get_legs(), "legs")

c = Cat()
c.set_color("Black")
c.set_legs(4)
print("This Cat has",c.get_color(), "color and", c.get_legs(), "legs")

r = Rabbit()
r.set_color("Black")
r.set_legs(4)
print("This Rabbit has",r.get_color(), "color and", r.get_legs(), "legs")

t = Tiger()
t.set_color("Yellow")
t.set_legs(4)
print("This Tiger has",t.get_color(), "color and", t.get_legs(), "legs")

l = Lion()
l.set_color("Silver")
l.set_legs(4)
print("This Lion has",l.get_color(), "color and", l.get_legs(), "legs")

p = Penguin()
p.set_color("Blue")
p.set_legs(2)
print("This Penguin has",p.get_color(), "color and", p.get_legs(), "legs")

g = Giraffe()
g.set_color("Yellow")
g.set_legs(4)
print("This Giraffe has",g.get_color(), "color and", g.get_legs(), "legs")

d = Dolphin()
d.set_color("Silver")
d.set_legs(0)
print("This Dolphin has",d.get_color(), "color and", d.get_legs(), "legs")

m = Monkey()
m.set_color("Silver")
m.set_legs(4)
print("This Monkey has",m.get_color(), "color and", m.get_legs(), "legs")

