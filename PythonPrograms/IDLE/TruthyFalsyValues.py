name=''
while not name :
    print("Enter the name")
    name=input()
    print("Welcome")
    print("How many guest are there")
    numOfGuest=int(input())
    if numOfGuest :
        print("Arrange rooms for :"+str(numOfGuest))

print("Execution done")
