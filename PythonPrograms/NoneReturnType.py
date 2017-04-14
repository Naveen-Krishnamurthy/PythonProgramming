def nonReturnType() : 
	value=5+6
	return value

def NonReturnedValue() :
	value =6*8
	return


print("Returned value :"+str(nonReturnType()))

nonReturnedvariable=NonReturnedValue()

print(nonReturnedvariable == None)