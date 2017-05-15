'''
Created on 11-May-2017

@author: ubuser
'''

from re import compile

def findPhoneNumber(message): 
    phoneNumberregEx=compile(r'\d{3}-\d{3}-\d{4}') # Passing our desired pattern format
    mo=phoneNumberregEx.search(message)
#     print(mo)
    if mo :
        print("Found phone number :"+mo.group())
    else :
        print("No phone number found")
    
findPhoneNumber("My phone number is 123-456-7891")
findPhoneNumber("Office phone number is 123-456-7891 and my phone number is 990-199-0541")
findPhoneNumber("message")



superHero=compile(r'Batman|Superman')
matchedHero=superHero.search("I'm a Superman")
print(matchedHero.group())
matchedHero=superHero.search("I'm a Batman")
print(matchedHero.group())
matchedHero=superHero.search("'Batman' vs \"Superman\"")
print(matchedHero.group())


#Mutliple matching using pipe
superHeroEquipement=compile(r'Bat(man|dress|bike|sticker|suite\|dress)')
matchedEquipement=superHeroEquipement.search("Batman")
print(matchedEquipement.group())
matchedEquipement=superHeroEquipement.search("Batdress")
print(matchedEquipement.group())
matchedEquipement=superHeroEquipement.search("Batbike")
print(matchedEquipement.group())
matchedEquipement=superHeroEquipement.search("Batsticker")
print(matchedEquipement.group())
matchedEquipement=superHeroEquipement.search("Batsuite|dress")
print(matchedEquipement.group())
print(matchedEquipement.group(1))


#Optional Matching
superHeroOptional=compile(r'Bat(wo)?man')
matchedOptional=superHeroOptional.search('I"m Batman')
print(matchedOptional.group())
matchedOptional=superHeroOptional.search("I'm Batwoman")
print(matchedOptional.group())

#Mutliple instance matching using *
superHeroMutliple=compile(r'Bat(wo)*man')
matchedMultiple=superHeroMutliple.search("I'm a Batman")
print(matchedMultiple.group())
matchedMultiple=superHeroMutliple.search("I'm Batwoman")
print(matchedMultiple.group())
matchedMultiple=superHeroMutliple.search("I'm Batwowowowowoman")
print(matchedMultiple.group())

#Matching 1 or one instance using '+'
superHeroMutliple=compile(r'Bat(wo)+man')
matchedMultiple=superHeroMutliple.search("I'm a Batman")
if matchedMultiple== None:
    print("No data")
matchedMultiple=superHeroMutliple.search("I'm Batwoman")
print(matchedMultiple.group())
matchedMultiple=superHeroMutliple.search("I'm Batwowowowowoman")
print(matchedMultiple.group())


