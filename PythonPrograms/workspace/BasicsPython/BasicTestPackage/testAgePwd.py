'''
Created on 08-May-2017

@author: ubuser
'''

#Validates the age
while(True) :
    print("Enter the age :")
    testValue=input()
    if(testValue.isdecimal()) :
        break
    print("Age is :"+repr(testValue))


#Validates the Pwd
while(True) :
    print("Enter the pwd (combination of number & alphabetics)")
    testValue=input()
    if testValue.isalnum() :
        break
    print("pwd is accepted")
