'''
Created on 09-May-2017

@author: ubuser
'''
from builtins import *

myPet=[]

while True :
    print("Enter the pet "+str(len(myPet))+"(or enter nothing to stop ):")
    testPet=input()
    if testPet=='':
        break
    myPet.append(testPet)
print(myPet)


for i in myPet :
    print(i)
    
print("Naveen" in myPet)
print("Arsenal" not in myPet)