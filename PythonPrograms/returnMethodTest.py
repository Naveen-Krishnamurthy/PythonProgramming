from random import *

def returnMethod(randNumber) :
	if(randNumber==1) :
		return "This is rand number 1"
	elif (randNumber == 2) :
		return "This is rand number 2"
	elif (randNumber == 3) :
		return "This is rand number 3"
	else :
		return "no value :"+str(randNumber)


for n in range(1,4) :
	r = randint(1,9)
	print("Return value is :"+returnMethod(r))
	print("Return the value in single line method call :"+returnMethod(randint(1,15)))