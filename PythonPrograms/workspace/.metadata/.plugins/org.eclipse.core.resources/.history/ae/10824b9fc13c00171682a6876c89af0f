'''
Created on 19-May-2017

@author: ubuser
'''

# Lambda function
square=lambda x: x*x
add = lambda x,y: x+y
sub=lambda x,y : x-y

print(square(2))
print(add(2,3))
print(sub(4,5))



#Lambda function used to calculate the List items as even or odd

myList=[1,3,5,8,44,6,9,11,12,16,20,7]

#Using the filter
evenList=list(filter(lambda x:(x%2==0),myList))
oddList=list(filter(lambda x:(x%2!=0),myList))

print("Using the filters")
print("Even list is ",evenList)
print("Odd list is ",oddList)

print("Using the maps")
evenList=list(map(lambda x:(x%2==0),myList))
oddList=list(map(lambda x:(x%2!=0),myList))
print("Even list is ",evenList)
print("Odd list is ",oddList)


#nonlocal keyword - Similar to global keyword, which is used to change the variable values within the nested function

def tstFun():
    a=5
    b=10
    print("Before changing the value ",a,b)
    def nestFun():
        a=10
        nonlocal b
        b=16
        print("After changing the value ",a,b)
    nestFun()
    print("Outside the nested function, the value is ",a,b)
    
tstFun()
