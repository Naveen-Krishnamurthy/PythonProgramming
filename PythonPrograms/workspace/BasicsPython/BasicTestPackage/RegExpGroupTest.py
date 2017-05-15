'''
Created on 11-May-2017

@author: ubuser
'''

from re import compile

def groupPhoneNumber(message):
    grpPhoneNumber=compile(r'(\d{3})-(\d{3}-\d{4})')
    matchedObject=grpPhoneNumber.search(message)
    if matchedObject :
        print("Phone number found")
        areaCode,phoneNumber=matchedObject.groups() # Returns tuple & again can be assigned to multiple variables using multi-assignment trick
        areaCodeWithFullNumber=matchedObject.group(0)
        areaCodeWithFullNumber2=matchedObject.group()
        print(areaCode)
        print(phoneNumber)
        print(areaCodeWithFullNumber)
        print(areaCodeWithFullNumber2)
        print(matchedObject.groups())
    else :
        print("Phone number not found")
        
groupPhoneNumber("This is my new phone number 990-199-0541")
groupPhoneNumber("message")