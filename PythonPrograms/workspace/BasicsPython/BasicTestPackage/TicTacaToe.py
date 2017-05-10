'''
Created on 10-May-2017

@author: ubuser
'''

from pprint import *

ticTacToe={
    'top-l':' ',
    'top-m':' ',
    'top-r':' ',
    'mid-l':' ',
    'mid-m':' ',
    'mid-r':' ',
    'low-l':' ',
    'low-m':' ',
    'low-r':' '
    }

#  Defination to format the board
def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])

printBoard(ticTacToe)
print()

#  Changing the data
ticTacToe={
    'top-l':'O',
    'top-m':'O',
    'top-r':'O',
    'mid-l':'X',
    'mid-m':'X',
    'mid-r':' ',
    'low-l':' ',
    'low-m':' ',
    'low-r':'X'
    }

printBoard(ticTacToe)
