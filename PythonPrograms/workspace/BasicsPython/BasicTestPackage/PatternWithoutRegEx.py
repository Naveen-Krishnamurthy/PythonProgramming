'''
Created on 11-May-2017

@author: ubuser
'''

#Method to check the valid phone number without using the regular expression in python

def checkPhoneNumber(phNumber): 
    if len(phNumber)!=12 :
        return False
    
    for i in range(0,3) :
        if not phNumber[i].isdecimal() :
            return False
        
    if phNumber[3]!='-' :
        return False
    
    for i in range(4,7) :
        if not phNumber[i].isdecimal() :
            return False
        
    if phNumber[7]!='-' :
        return False
    
    for i in range(8,12) :
        if not phNumber[i].isdecimal() :
            return False    
    return True

print(checkPhoneNumber("ABCE"))  
print(checkPhoneNumber("XXX-XXX-XXXX")) 
print(checkPhoneNumber("123-XXX-XXXX")) 
print(checkPhoneNumber("123-456-XXXX"))  
print(checkPhoneNumber("123-456-7894"))  
print(checkPhoneNumber("123456789444")) 


message="This is my phone Number 990-199-0541 & my office phone number is 123-456-7891"

for i in range(0,len(message)) :
    checkNum=message[i:i+12]
    if checkPhoneNumber(checkNum) :
        print("Phone number found :"+checkNum)


 