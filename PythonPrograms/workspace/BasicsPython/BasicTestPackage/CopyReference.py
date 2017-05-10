'''
Created on 10-May-2017

@author: ubuser
'''

from copy import *


refList=[1,2,3,4,5,6]
print(refList)
spam=copy(refList)
spam.append("NewValue")
print(refList)
print(spam)


# DeepCopyTest

deepCopyList=[1,2,3,4,["Naveen","Welcome"]]
print(deepCopyList)
deepSpamCopy=deepcopy(deepCopyList)
deepSpamCopy.append("Testing")
print(deepCopyList)
print(deepSpamCopy)