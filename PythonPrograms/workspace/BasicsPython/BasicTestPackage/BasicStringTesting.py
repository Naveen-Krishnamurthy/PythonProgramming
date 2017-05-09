'''
Created on 05-May-2017

@author: ubuser
'''


print("This is new String")
print('Strings can be represented using single quote')
print('If there is "double quote" inside string value, it can be represented or enclosed within single quote')
print("If there is 'Single quote' inside string value, it can be represented or enclosed within double quote")
print("If we want to represent both \"double\" & \'single\' quote we should be using the escape characters")
print("This is how we print the new line \n from here it will be displayed in new line")
print(r"Normal path can be convered to new line string because of escape character c:python\newpath ")


# Accessing characters of String

value='This is my String literal'
print(value)
print("5th Character :"+value[5])
print("1st Character :"+value[0])
print("5th character from last :"+value[-5])

# String slicing(Substring)

print("Get the string from 4th position to 14th position :"+value[3:13])
print("Get the complete string from :"+value[:])
print("Only Start point in slicing :"+value[5:])
print("Only end point in the slice :"+value[:14])
print("Invalid start & stop :"+value[-5:0])
print("Length of the string in variable :"+repr(len(value)))
print("Length of the string is :"+repr(len('asdfasdfasdfasdf')))


# Multiline String
multilineString="""This is multiline string 
which can be used in multiple lines. 
The Start & end of the multiline string should be 
using the 3 \" or \' qoutes in it """

# Membership Operators used for String
print(multilineString)
print("This" in multilineString)
print("Naveen" not in multilineString)
print("Test" in multilineString)

# UserfulMethods in String

upperCaseValue=multilineString.upper()
lowerCaseValue=multilineString.lower()

print(upperCaseValue)
print(lowerCaseValue)

print("String variable 'upperCaseValue' is upper :"+repr(upperCaseValue.isupper()))
print("String variable 'lowerCaseValue' is lower :"+repr(lowerCaseValue.islower()))

alphaValue="WelcomeToPython!"
alphaNumValue="WelcomeToPython!123456"
decimalValue="123456789"
stringWithSpace="Naveen/n"
print("Alpha vlaue :"+repr(alphaNumValue.isalpha()))













