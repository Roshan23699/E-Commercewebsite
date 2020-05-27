from shape_module import triangle as T
from shape_module import regular_polygon
import math, turtle, time

class regular_hexagon(regular_polygon):

	def __init__(self, l):
		super().__init__(6,l,"Regular Hexagon")

	def set_dimension(self, l):
		self._len = l

	def get_dimension(self):
		super().get_dimension()

	def get_perimeter(self):
		super().get_perimeter()

	def get_area(self):
		k = 1.5 * math.sqrt(3)
		self._area = k * (self._len ** 2)
		print("Area : {:.3f} sq. units".format(self._area))

	def get_sum_of_angles(self):
		super().get_sum_of_angles()

	def draw(self):
		super().draw()

class regular_pentagon(regular_polygon):

	def __init__(self, l):
		super().__init__(5,l, "Regular Pentagon")

	def set_dimension(self, l):
		self._len = l

	def get_dimension(self):
		super().get_dimension()

	def get_perimeter(self):
		super().get_perimeter()

	def get_area(self):
		k = 1.5 * math.sqrt(3)
		self._area = k * (self._len ** 2)
		print("Area : {:.3f} sq. units".format(self._area))

	def get_sum_of_angles(self):
		super().get_sum_of_angles()

	def draw(self):
		super().draw()


class regular_octagon(regular_polygon):

	def __init__(self, l):
		super().__init__(8,l,"Regular Octagon")

	def set_dimension(self, l):
		self._len = l

	def get_dimension(self):
		super().get_dimension()

	def get_perimeter(self):
		super().get_perimeter()

	def get_area(self):
		k = 2 * (math.sqrt(2) + 1)
		self._area = k * (self._len ** 2)
		print("Area : {:.3f} sq. units".format(self._area))

	def get_sum_of_angles(self):
		super().get_sum_of_angles()

	def draw(self):
		super().draw()


class equilateral(T):

	def __init__(self, side):
		self.__type = "Equilateral Triangle"
		self.set_dimension(side)
		print("Type : {}".format(self.__type))

	def set_dimension(self, side):
		self.__l1 = self.__l2 = self.__l3 = side

	def get_dimension(self):
		print("Dimensions are : {}, {}, {}".format(self.__l1, self.__l2, self.__l3))

	def get_area(self):
		self.__area = 0.866 * (self.__l1 ** 2)		
		print("Area : {} sq. units".format(self.__area))

	def get_perimeter(self):
		self.__perimeter = self.__l1 + self.__l2 + self.__l3
		print("Perimeter = {} units".format(self.__perimeter))

	def draw(self):
		t = turtle.Turtle()
		t.pensize(2)
		t.penup()
		t.right(135)
		t.forward(200)
		t.pendown()
		t.left(135)
		for i in range(3):
			t.forward(self.__l1)
			t.left(120)
		time.sleep(2)
		t.clear()	


class right_angle(T):

	def __init__(self, l1, l2, l3):
		self.__type = "Right Angle Triangle"
		l = [l1, l2, l3]
		l.sort()
		l1, l2, l3 = l
		self.set_dimension(l1, l2, l3)
		print("Type : {}".format(self.__type))

	def set_dimension(self, l1, l2, l3):
		self.__l1, self.__l2, self.__l3 = l1, l2, l3

	def get_dimension(self):
		print("Dimensions are : {}, {}, {}".format(self.__l1, self.__l2, self.__l3))

	def get_area(self):
		self.__area = 0.50 * (self.__l1 * self.__l2)		
		print("Area : {} sq. units".format(self.__area))

	def get_perimeter(self):
		self.__perimeter = self.__l1 + self.__l2 + self.__l3
		print("Perimeter = {} units".format(self.__perimeter))


class scalene(T):

	def __init__(self, l1, l2,l3):
		self.__type = "Scalene Triangle"
		self.set_dimension(l1, l2, l3)
		print("Type : {}".format(self.__type))

	def set_dimension(self, l1, l2, l3):
		self.__l1, self.__l2, self.__l3 = l1, l2, l3

	def get_dimension(self):
		print("Dimensions are : {}, {}, {} units".format(self.__l1, self.__l2, self.__l3))

	def get_area(self):
		s = self.__perimeter / 2
		self.__area = math.sqrt(s * (s - self.__l1) * (s - self.__l2) * (s - self.__l3))	
		print("Area : {} sq. units".format(self.__area))

	def get_perimeter(self):
		self.__perimeter = self.__l1 + self.__l2 + self.__l3
		print("Perimeter = {} units".format(self.__perimeter))

class circle:

	def __init__(self, radius):
		self.__radius = radius
		print("Type : Circle")

	def set_radius(self, r):
		self.__radius = r

	def get_radius(self):
		return self.__radius

	def draw(self):
		c = turtle.Turtle()
		c.pensize(2)
		c.circle(self.__radius)
		time.sleep(2)
		c.clear()

########################################################################################################

class rectangle:

	def __init__(self, length, breadth):
		self.__length = max(length, breadth)
		self.__breadth = min(length, breadth)
		print("Tyep : Rectangle")

	def get_dimension(self):
		print("Length : {} \t Breadth : {}".format(self.__length, self.__breadth))

	def get_perimeter(self):
		self.__perimeter = 2 * (self.__length + self.__breadth)
		print("Perimeter : {} units.".format(self.__perimeter))

	def get_area(self):
		self.__area = self.__length * self.__breadth
		print("Area : {} sq. units.".format(self.__area))

	def get_diagonal(self):
		self.__diagonal = math.sqrt(self.__length ** 2 + self.__breadth ** 2)
		print("Diagonal : {:.2f} units.".format(self.__diagonal))

	def draw(self):
		t = turtle.Turtle()
		t.pensize(2)
		l, b, d = self.__length, self.__breadth, self.__diagonal
		for i in range(4):
			if(i % 2 == 0):
				t.forward(l)
				t.left(90)
			else:
				t.forward(b)
				t.left(90)

		theta = math.atan(self.__breadth / self.__length) * 57.295
		t.left(theta)
		t.forward(d)
		time.sleep(2)
		t.clear()

class square(rectangle):

	def __init__(self, side):
		super().__init__(side, side)
		self.__side = side
		print("Type : Square")

	def get_dimension(self):
		print("Side : {} units".format(self.__side))


if __name__ == '__main__':

	c1 = circle(100)
	c1.draw()
	print("Radius : {} units".format(c1.get_radius()))
	print("\n")

	r1 = rectangle(200, 100)
	r1.get_dimension()
	r1.get_area()
	r1.get_perimeter()
	r1.get_diagonal()
	r1.draw()
	print("\n")

	r = square(250)
	r.get_dimension()
	r.get_area()
	r.get_perimeter()
	r.get_diagonal()
	r.draw()
	print("\n")

	e = equilateral(200)
	e.get_dimension()
	e.get_perimeter()
	e.get_area()
	e.draw()
	print("\n")

	r = right_angle(4,3,5)
	r.get_area()
	r.get_perimeter()
	r.get_dimension()
	print("\n")

	s = scalene(6,6,8)
	s.get_perimeter()
	s.get_area()
	s.get_dimension()
	print("\n")

	r_p = regular_pentagon(200)
	r_p.draw()
	r_p.get_area()
	r_p.get_perimeter()
	r_p.get_sum_of_angles()
	print("\n")

	r_h = regular_hexagon(150)
	r_h.draw()
	r_h.get_area()
	r_h.get_perimeter()
	r_h.get_sum_of_angles()
	print("\n")

	r_o = regular_octagon(150)
	r_o.draw()
	r_o.get_area()
	r_o.get_perimeter()
	r_o.get_sum_of_angles()
	print("\n")
	
	

