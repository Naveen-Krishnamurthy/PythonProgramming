'''
Created on 10-May-2017

@author: ubuser
'''

from pprint import *

nestDic={
    "Naveen":{'Black-Dog':3,'Blenderspide':2,'Henkinse':1},
    "Sukesh":{'Teachers':2,'Blenderspide':1,'Black-Dog':1},
    "Bhaskar":{'Black-Dog':4,'Blenderspide':2,'Teachers':3}
    }

pprint(nestDic)

def countBeverage(guest,item):
    numberOfBeverage=0
    for k,v in guest.items() :
        numberOfBeverage+=v.get(item,0)
    return numberOfBeverage    

print(countBeverage(nestDic,"Black-Dog"))

testDict={"Cat":"Yes"}
print("Cat" in testDict)
print("Cat" in testDict.keys())
print("Cat" in testDict.values())
print("Cat" in testDict.items())