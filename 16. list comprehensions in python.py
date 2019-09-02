name="alejandro"
mylist=[]
for letter in name:
	mylist.append(letter)
print(mylist)
print("")

# we can rewrite the same above as below
mylist2= [letter for letter in name]
print(mylist2)
print("")

mylist3=[num for num in range(5)]
print(mylist3)





