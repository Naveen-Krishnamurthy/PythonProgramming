def divideByZero(testData) :
	try :
		value=42/testData
		print(value)
	except ZeroDivisionError :
		print("Caught exception")

divideByZero(12)
divideByZero(3)
divideByZero(0)
divideByZero(10)