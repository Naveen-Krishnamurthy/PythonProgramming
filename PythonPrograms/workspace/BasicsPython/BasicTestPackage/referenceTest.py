'''
Created on 10-May-2017

@author: ubuser
'''

spam=42
print(spam)
chees=spam
chees=100
print(spam)
print(chees)


# Reference to list

testList=[1,2,3,6]
print(testList)
newList=testList
newList[1]=56
print(newList)
print(testList) 


def testList(passByRefer):
    passByRefer.append("Pass by reference Test")
    
    
passByReference=[1,2,3,4,5]
print("Before passBy reference :"+repr(passByReference))
testList(passByReference)
print("After passBy reference :"+repr(passByReference))