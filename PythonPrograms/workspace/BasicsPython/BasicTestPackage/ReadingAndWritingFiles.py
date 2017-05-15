'''
Created on 13-May-2017

@author: ubuser
'''


from os import path,chdir, makedirs, listdir
from posix import getcwd

# This method will return the path based on OS that we are using, if we execute the same in Windows machine it will return the path according to Windows Machine
ActualPath=path.join("user","xxx","Documents")
print(ActualPath)


'''
/home/ubuser/Documents/PythonProgramming/PythonPrograms/workspace
This will join the filenames in the list with the path that we have mentioned.
'''

fileName=["test.txt","Document.docx","pythonBasic.pdf"]
for file in fileName :
    AbsoluteFilePath=path.join('/home/ubuser/Documents/PythonProgramming/PythonPrograms/workspace',file)
    print("Absolute path is :"+path.abspath(AbsoluteFilePath))
    print(path.isabs(AbsoluteFilePath))
    print("Relative path is :"+path.relpath(AbsoluteFilePath))
    print(AbsoluteFilePath)


# Current Working directory & change the working directory

print("Current working directory "+getcwd())
print("Absolute path of current working directory :"+path.abspath(getcwd()))
print("Current working directory is absolute :"+repr(path.isabs(getcwd())))
print("Relative path of current working directory :"+path.relpath(getcwd(),"/home/ubuser/Documents"))

#User of dirname & baseName
testPath=getcwd()+"/NewFolder/test.xlsx"
print("Directory name is :"+path.dirname(testPath))
print("Base file/folder name is :"+path.basename(testPath))



print(getcwd())
relativePath=path.relpath("/home/ubuser/Documents/PythonProgramming/PythonPrograms/workspace/BasicsPython/BasicTestPackage")
print("Relative path is :"+relativePath)
absolutePath=path.abspath('.')
print("Absolute path is :"+absolutePath)
print(path.isabs(relativePath))
print(path.isabs(absolutePath))

#Basename
print(path.basename(absolutePath))

#Dirname
print(path.dirname(absolutePath))

#Splitting the paths
baseNameDirName=absolutePath.split(path.sep)
print("Tuple is :"+repr(baseNameDirName))

#Get the file size & file contents
FilePathWithFile="/home/ubuser/Documents/PythonProgramming/PythonPrograms/Circle.py"
FilePathWithoutFile="/home/ubuser/Documents/PythonProgramming/PythonPrograms"

print(path.getsize(FilePathWithFile))
print(path.getsize(FilePathWithoutFile))
print("List of the folder contents is :"+repr(listdir(FilePathWithoutFile)))

#Sample to get the list of files in the folder & total contents
totalSize=0

for fileName in listdir(FilePathWithoutFile) :
    print("File name :"+fileName+" and the size is :"+repr(path.getsize(path.join(FilePathWithoutFile,fileName))))
    totalSize=totalSize+path.getsize(path.join(FilePathWithoutFile,fileName))

print("Total size of the folder is :"+repr(totalSize))


#Checking the file & folder existence
print("It is a file :"+repr(path.isfile(FilePathWithFile)))
print("It is a file :"+repr(path.isfile(FilePathWithoutFile)))
print("It is a folder :"+repr(path.isdir(FilePathWithoutFile)))
print("It is a folder :"+repr(path.isdir(FilePathWithFile)))

print("Is file exist "+repr(path.exists(FilePathWithFile)))
print("Is folder exist :"+repr(path.exists(FilePathWithoutFile)))

#Reading the File all in one line 
readFilePath="/home/ubuser/Documents/PythonProgramming/PythonPrograms/TestDocument"
print("Is the file :"+repr(path.isfile(readFilePath)))
fileObject=open(readFilePath)
print("File object is :"+repr(fileObject))
print("Read the file :"+repr(fileObject.read()))
fileObject.close()

#Reading the files line by line
fileObject=open(readFilePath)
lineList=fileObject.readlines()
print(lineList)
fileObject.close()

#Creating new file using Write mode
fileObject=open("/home/ubuser/Documents/PythonProgramming/PythonPrograms/TestDocument1",'w')
fileObject.write("Creating the new file\n")
fileObject.write("Line 2 added using the write mode\n")
fileObject.close()

#Reading the file in readmode now
fileObject=open("/home/ubuser/Documents/PythonProgramming/PythonPrograms/TestDocument1",'r')
NumberOfLines=fileObject.readlines()
print(NumberOfLines)
fileObject.close()

#ReWriting the file using write mode again
fileObject=open("/home/ubuser/Documents/PythonProgramming/PythonPrograms/TestDocument1",'w')
fileObject.write("Test1\n")
fileObject.write("Test2\n")
fileObject.write("Test3\n")
fileObject.close()

#Reading them again
fileObject=open("/home/ubuser/Documents/PythonProgramming/PythonPrograms/TestDocument1",'r')
NumberOfLines=fileObject.readlines()
print(NumberOfLines)
fileObject.close()

#Append mode
fileObject=open("/home/ubuser/Documents/PythonProgramming/PythonPrograms/TestDocument1",'a')
fileObject.write("Adding the new Line")
fileObject.close()

#Reading the appended files
fileObject=open("/home/ubuser/Documents/PythonProgramming/PythonPrograms/TestDocument1",'r')
NumberOfLines=fileObject.readlines()
print(NumberOfLines)
fileObject.close()











