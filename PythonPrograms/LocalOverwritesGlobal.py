print("First time ",end=':')
name='naveen'
print(name)
def insideMethod() :
	print(name)
	print("inside the method :"+name)

insideMethod()
print("outside method ",end=':')
print(name)
