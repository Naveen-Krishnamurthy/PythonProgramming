print("Enter the username :")
username=input()
print("Enter the pwd:")
pwd=input()

if(username=='Naveen') :
    print(username+" is authorized, but pwd?")
    if(pwd=='Welcom') :
        print("Successful "+username)
    elif(pwd=='notwelcome') :
        print("Failure, wrong pwd")
    else :
        print("Invalid pwd")
elif(username=='Girish') :
    print(username +" is authorized, but pwd ?")
    if(pwd=='Welcom') :
        print("Successful "+username)
    elif(pwd=='notwelcome') :
        print("Failure, wrong pwd")
    else :
        print("Invalid pwd")
