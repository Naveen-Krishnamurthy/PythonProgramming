'''
Created on 08-May-2017

@author: ubuser
'''


def printPicnic(itemDict,leftWidth,rightWidth): 
    print("Print Picnic".center(leftWidth+rightWidth,'*'))
    for k,v in itemDict.items() :
        print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth,' '))
    
picnicDict={"Apple":1,"Graphes":2,"Mango":3,"JackFruite":4}
printPicnic(picnicDict,15,11)