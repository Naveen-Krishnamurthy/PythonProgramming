'''
Created on 11-May-2017

@author: ubuser
'''

from re import compile

greedyPatternMatching=compile(r'(Ha){3,5}?')
testMatchObject=greedyPatternMatching.search("Welcome to New HaHaHaHaHa Program")
if testMatchObject != None :
    print(testMatchObject.group())
else :
    print("No match found")

#Returning the list of matches if there are not groups in the regex pattern
listOfMatches=compile(r'\d{3}?-\d{3}-\d{4}')
testMatchObjectList=listOfMatches.findall("My phone number is 990-199-0541 and my office phone number is 123-456-7891 and without area code it is 456-7894")
if testMatchObject != None :
    print(testMatchObjectList)
else :
    print(" No match found")
 