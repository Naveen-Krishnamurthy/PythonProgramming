class ArthOperation :
	a=10
	b=20

	def add(self) :
		return self.a+self.b

	def sub(self) :
		return self.a-self.b

	def square(self) :
		return self.a * self.a

	def differentNumber(self) :
		self.a=40



obj1= ArthOperation() 
print("Addition is :"+repr(obj1.add()))
print("Addition is :"+repr(obj1.sub()))
print(ArthOperation.a)
print("Square is :"+repr(obj1.square()))
obj1.differentNumber()
print("Here you go :"+repr(obj1.a))