from math import *

class Circle : 
	def __init__(self, radius) :
		self.radius=radius

	def area(self) :
		return pi * self.radius**2

class CirclePlus(Circle) : 
	def __init__(self,radius) :
		super(CirclePlus,self).__init__(radius)

	def daimeter(self) :
		return self.radius*2

	def circumference(self) : 
		return self.radius*2*pi


c=Circle(3)
print(c.area())
print(c.radius)

c1=CirclePlus(7)
print(c1.radius)
print(c1.daimeter())