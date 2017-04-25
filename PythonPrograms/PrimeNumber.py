
class testPrime : 
	def function_Range(self) :
		for n in range(2,10) :
			for x in range(2,n) :
				if n % x==0 :
					print(n,"is not a prime number")
					break
				else :
					print(n,"is a prime number")



	def function_EvenNumber(self) :
		for n in range (1,10,2) :
			if n % 2 == 0 : 
				print(n, "is a even number")
				continue
			print(n, "is not a even number")


	def testWhile_Else(self) : 
		while(counter<3) :
			print("Inside the while loop ")
			counter=counter+1
			if(counter==3) :
				break

		else
			print("Inside while else loop")


obj1=testPrime()
print("Prime number Testing")
obj1.function_Range()
print('\n')
print("Even number testing")
obj1.function_EvenNumber()




