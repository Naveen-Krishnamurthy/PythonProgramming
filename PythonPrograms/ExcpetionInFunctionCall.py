def excepitonInFunCall(value) :
	print("value is :"+str(value))
	print("Divided is :"+str(36/value))

try :
	excepitonInFunCall(10)
	excepitonInFunCall(20)
	excepitonInFunCall(0)
	excepitonInFunCall(3)
except ZeroDivisionError :
	print("Caught the exception in function call ")
