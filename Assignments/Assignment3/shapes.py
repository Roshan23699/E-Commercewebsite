import turtle
class Circle:
    def __init__(self, r = 0):
        self.__radius = r
    def set_radius(self, r):
        self.radius = r
    def get_radius(self):
        return (self.radius)
    def find_area(self):
        pi = 3.14
        return (pi * self.radius * self.radius)
    def draw(self):
        t = turtle.Turtle()
        t.circle(self.radius)
        turtle.done()
        
class Heptagon:
    def __init__(self, s = 0):
        self.__side = s
    def set_side(self, s):
        self.side = s
    def get_side(self):
        return self.side
    def draw(self):
        t = turtle.Turtle()
        for i in range(7):
            t.forward(self.side)
            t.right(51.42)
        turtle.done()
        
class Hexagon:
    def __init__(self, n = 0, l = 0):
        self.num = n
        self.length = l
    def set_props(self, n, l):
        self.num = n
        self.length = l
    def draw(self):
        t = turtle.Turtle()
        angle = 360.0 / self.num

        for i in range(self.num):
            t.forward(self.length)
            t.right(angle)

        turtle.done()
        
class Line:
    def __init__(self, l = 0):
        self.__length  = l
    def get_length(self):
        return  self.length
    def set_length(self, l):
        self.length = l
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.length)
        turtle.done()
        
class Nanogon:
    def __init__(self, s = 0):
        self.__side = s
    def set_side(self, s):
        self.side = s
    def get_side(self):
        return self.side
    def draw(self):
        t = turtle.Turtle()
        for i in range(9):
            t.forward(self.side)
            t.right(40)
        turtle.done()

class Octagon:
    def __init__(self, s = 0):
        self.__side = s
    def set_side(self, s):
        self.side = s
    def get_side(self):
        return self.side
    def draw(self):
        t = turtle.Turtle()
        for i in range(8):
            t.forward(self.side)
            t.right(45)
        turtle.done()
        
class Pentagon:
    def __init__(self, n = 0, l = 0):
        self.num = n
        self.length = l
    def set_props(self, n, l):
        self.num = n
        self.length = l
    def draw(self):
        t = turtle.Turtle()
        angle = 360.0 / self.num

        for i in range(self.num):
            t.forward(self.length)
            t.right(angle)

        turtle.done()
        
class Rectangle:
    def __init__(self, l = 0, w = 0):
        self.__length = l
        self.__width = w
    def set_side(self, l, w):
        self.length = l
        self.width  = w
    def get_area(self):
        return (self.length * self.width)
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.length)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.length)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        
class square():
	def __init__(self,a = 5):
		self.__side = a

	def get_side(self):
		return self.__side

	def find_area(self):
		return (self.__side * self.__side)

	def find_perimeter(self):
		return(4 * self.__side)

	def draw(self):
		t = turtle.Turtle()
		t.forward(self.__side)
		t.left(90)
		t.forward(self.__side)
		t.left(90)
		t.forward(self.__side)
		t.left(90)
		t.forward(self.__side)
		t.left(90)
		turtle.done()


class Triangle:
    def __init__(self, s1 = 0, s2 = 0, s3 = 0):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
    def set_side(self, s1, s2, s3):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
    def get_side(self):
        return (self.side1, self.side2, self.side3)
    def get_perimeter(self):
        return (self.side1 + self.side2 + self.side3)
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.side1)
        t.left(120)
        t.forward(self.side2)
        t.left(120)
        t.forward(self.side3)
       # t.left(120)
        turtle.done()
        
        
n = Nanogon()
n.set_side(100)
n.draw()
