class testInheritance1 : 
	def testMethod() : 
		print("This is method of testInheritance1 ")


class testInheritance2 : 
	def testMethod() : 
		print("This is method of testInheritance2 ")


class testInhertiance3 : 
	def testMethod() : 
		print("This is method of testInheritance3 ")


class overload(testInheritance2, testInhertiance3, testInheritance1) : 
	def testMethod() : 
		print("This method belongs to child of 3 parents")


overload.testMethod()