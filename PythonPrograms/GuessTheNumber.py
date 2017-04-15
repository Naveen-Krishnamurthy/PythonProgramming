from random import *

screetNumber=randint(1,20)

#Ask user to enter the number


for guessNumber in range(1,6) :
	print("Guess the number ",end=':')
	value=int(input())
	if(value > screetNumber) :
		print("Your number is too high :"+str(value))
	elif(value<screetNumber) :
		print("Your number is too low :"+str(value))
	elif(value==screetNumber) :
		print("perfect Match :"+str(value))
		break
	else :
		print("Timeout")


print("Guessing Game done")

