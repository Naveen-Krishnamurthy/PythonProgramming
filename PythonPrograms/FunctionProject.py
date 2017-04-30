#Return the value based on even & odd number
def checkNum(val) : 
	if(val%2==0) :
		return int(val//2)
	elif(val%2==1) :
		return int(3*val + 1)


def testMethod() :
	retValue=0
	while retValue!=1 :
		try : 
			print("Please enter the number : ")
			num=int(input())
			retValue=checkNum(num)
			print("The returned number is : "+str(retValue))
		except ValueError : 
			print("Error :enter the valid number")

testMethod()


