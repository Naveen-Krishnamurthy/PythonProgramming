'''
Created on 11-May-2017

@author: ubuser
'''

from re import compile,DOTALL

chacterClass=compile(r'\d+\_\w+')
matchedCharacterClass=chacterClass.findall("12_Tweleve 11 Eleven 10_Ten 9_Nine")
print(matchedCharacterClass)


#  Own Character class
vowelTest=compile(r'[aeiouAEIOU]')
matchedVowels=vowelTest.findall("Arsenal is the best team i ever saw, i'm fan of arsenal. Python is very good language")
print(matchedVowels)
negativeVowelTest=compile(r'[^aeiouAEIOU]')
matchedVowels=negativeVowelTest.findall("Arsenal is the best team i ever saw, i'm fan of arsenal. Python is very good language")
print(matchedVowels)

#Caret & Dollar used for starts with & ends with

caretDollar=compile(r'Ars$')
matchedStartsWith=caretDollar.search("Gunners is good team & Arsen wenger is the bossArs")
print(matchedStartsWith.group())



# Wild card character for the
wildCard=compile(r'.at')
matchedWildCard=wildCard.findall("Cat is a bat but at this is rat hat")
print(matchedWildCard)

#  Using Wildcard to match for new line
wildCardNewLine=compile(r'.*',DOTALL)
matchedWildCard=wildCardNewLine.findall("This is my sentence having \nnew line which will be printed as it is")
print(matchedWildCard)