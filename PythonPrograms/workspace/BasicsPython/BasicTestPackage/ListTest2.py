'''
Created on 08-May-2017

@author: ubuser
'''


spam=['cat','bat','rat','elephant']
print(spam[3])
print([1,2,3,4][2])
print("Hello "+spam[0])
print("Here are the animals :"+spam[0]+","+spam[1]+","+spam[2]+","+spam[3])


spam.append([1,2,3,4])

print(spam)
print(spam[4])
print(spam[4][3])
print(spam[-1][-3])

testList=[1,4,5,"Naveen",True,36.5]
print(testList)
del testList[3]
print(testList)