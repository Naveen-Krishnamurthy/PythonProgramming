'''
Created on 08-May-2017

@author: ubuser
'''

#List Values
players=[10,16,11,17]
print(players)
print(players[-3])
players[2]=10
print(players)
print(players+[3,4,5])
print(players)
players.append(45)
print(players)
testplayers=[4,5,6]
players.append(testplayers)
print(players)
print(players[1:])
print(players[:2])

players[2:4]=[]
print(players)

