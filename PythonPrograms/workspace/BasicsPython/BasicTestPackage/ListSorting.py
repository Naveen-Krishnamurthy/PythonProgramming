'''
Created on 09-May-2017

@author: ubuser
'''


testList=["apple","Apple","zebra","Zebra","Dog"]
print(testList)
testList.sort()
print(testList)
testList.sort(key=str.lower)
print(testList)