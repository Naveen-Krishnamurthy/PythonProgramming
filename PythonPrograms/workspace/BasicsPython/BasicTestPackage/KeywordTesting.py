'''
Created on 19-May-2017

@author: ubuser
'''

# globVariable=10
# 
# def read():
#     print(globVariable)
# 
# 
# def write():
#     global globVariable
#     globVariable=99
#     
# def write2(): 
#     globVariable=123
#     
# 
# read()
# write()
# read()
# write2()
# read()
# 
# 
# print("Identity operators use")
# 
# print(True is True)
# print(True == True)
# print(False is False)
# print(False == False)
# print(None == None)
# print(None is None)
# 
# print({}=={})
# print({} is {})
# 
# value1=99
# value2=99
# 
# print(value1==value2)
# print(value1 is value2)



# yield testing

def square():
    for i in range(10) :
        return i*i


def genSquare():
    for i in range(10) :
        yield i*i

value=square()
print(value)

genValue=genSquare()
print(next(genValue))
for i in genValue :
    print("Vaue is ",i)
    

#Generator syntax 
g=(2**x for x in range(2))
print(next(g))
print(next(g))