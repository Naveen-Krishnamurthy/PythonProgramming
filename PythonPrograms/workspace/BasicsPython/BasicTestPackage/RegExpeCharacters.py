'''
Created on 11-May-2017

@author: ubuser
'''

from re import compile

matchingPattern=compile(r'\w+@\w+.\w+')# Matching the email address
testMailMatchObject=matchingPattern.search("This is valid emial address Naveen3665@hotmail.com, Naveen3665@gmail.com,Naveen.Krishnamurthy@sony.com")
if testMailMatchObject != None :
    print(testMailMatchObject.group())
else :
    print("Not a valid email address")
    
#Using Find all
testMailMatchObject=matchingPattern.findall("This is valid email address Naveen3665@hotmail.com, Naveen3665@gmail.com,NaveenKrishnamurthy@sony.com")
if testMailMatchObject != None :
    print(testMailMatchObject)
else :
    print("Not a valid email address")