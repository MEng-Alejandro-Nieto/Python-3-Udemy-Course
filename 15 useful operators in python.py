# USEFUL OPERATORS IN PYTHON


#				range
for num in range(10):
	print (num)
print("")

for num in range(4,10):
	print (num)
print("")

for num in range(4,10,2):
	print (num)
print("")

# 				list 
mylist=list(range(15))
print(mylist)
print("")

#				enumarate
word="abcde"
for item in enumerate(word):
	print(item)
print("")

#				ZIP
mylist1=[1,2,3]
mylist2=["a","b","c"]
for item in zip(mylist1,mylist2):
	print(item)


#				key
a="a" in "avengers"
print(a)
print("")


#			min / max
mylist=[1,2,3,4,5,6,7,8,9]
a=min(mylist)
b=max(mylist)
print(f"the maximum values is {b} and the minimum values is {a}")
print("")

# 				import libraries
mylist=[1,2,3,4,5,6,7,8,9]
from random import shuffle
shuffle(mylist)
print(mylist)



#				input
a=input("entera a number to play with")
a=int(a)
for num in range(a):
	print(num)


