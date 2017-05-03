listWk=['sun','mon','tus','wed','thur','fri','sat']
listAsTuple=tuple(listWk)
print(listAsTuple)

x,y=35,75
smaller=x if x < y else y
print(smaller)

def testLIst(val,list=[]) : 
	list.append(val)
	return list


def testList2(val,list=None) : 
	if list is None : 
		list=[]
	list.append(val)
	return list

list3=testLIst('a')
list4=testList2('a')
list5=testList2(123,[])

print(list3)
print(list4)
print(list5)




fruit={}

def addOn(Index) :
	if Index in fruit :
		fruit[Index]+=1
	else : 
		fruit[Index]=1

addOn('Apple')
addOn("Bannan")
print(len(fruit))


ar={}
ar[1]=1
ar['1']=2
ar[1]+=1

sum=0
for k in ar : 
	sum+=ar[k]

print(sum)

dict={'a':1}
for i in sorted(dict) :
 print(i)

 x=float(input("your number"))
 inverse=1.0/x

 