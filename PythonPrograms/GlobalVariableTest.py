def globalTest() :
	global name
	name="Naveen"
	print(name)
	callAgain()
	print(name)


def callAgain() :
	global name
	name='Girish'
	print(name)

name='NewName'
globalTest()
print(name)

