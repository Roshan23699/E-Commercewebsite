from abc import ABC, abstractmethod
import turtle, time

class triangle(ABC):

	@abstractmethod
	def __init__(self, type):
		self.__type = type

	@abstractmethod
	def set_dimension(self, a, b, c):
		self.__l1 = a
		self.__l2 = b
		self.__l3 = c

	@abstractmethod
	def get_dimension(self):
		print("Dimensions are : {}, {}, {}".format(self.__l1, self.__l2, self.__l3))

	@abstractmethod
	def get_perimeter(self):
		pass

	@abstractmethod
	def get_area(self):
		pass



class regular_polygon(ABC):

	@abstractmethod
	def __init__(self, n_sides, length, type = None):
		self._sides = n_sides
		self.set_dimension(length)
		self._area = None
		self._soa = 180 * (self._sides - 2)
		self._type = type
		self.type()

	def type(self):
		print("{}. \t Side = {} units".format(self._type, self._len))

	@abstractmethod
	def set_dimension(self, length):
		self._len= length

	@abstractmethod
	def get_dimension(self):
		print("Length is : {} units".format(self._len))

	@abstractmethod
	def get_perimeter(self):
		self._perimeter = self._sides * self._len
		print("Perimeter is : {}".format(self._perimeter))

	@abstractmethod
	def get_area(self):
		pass

	@abstractmethod
	def get_sum_of_angles(self):
		print("Sum of angles : {} degrees.".format(self._soa))

	@abstractmethod
	def draw(self):
		t = turtle.Turtle()
		t.pensize(2)
		t.penup()
		t.right(135)
		t.forward(200)
		t.pendown()
		t.left(135)
		theta = 360 / self._sides
		for i in range(self._sides):
			t.forward(self._len)
			t.left(theta)
		time.sleep(2)
		t.clear()

