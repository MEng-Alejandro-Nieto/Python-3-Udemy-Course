mylist =[1,2,3,4,5,6,7,8,9,10]
for num in mylist:				# it can be num or another word
	print(num)
print("")

for element in mylist:				# it can be num or another word
	print("hello")
print("")

for letter in "animal":
	print(letter)

# lets print out only the even number in "my list"
print("")
for even in mylist:
	if even%2==0:
		print(even)
print("")

#  lets now print out all numbers but also show if the number is odd or even
for even in mylist:
	if even%2==0:
		print(f"{even} is even")
	else:
		print(f"{even} is odd")
print("")

# creat a loop that calculate the sum of all the numbers inside "my list"
suma=0
for num in mylist:
	suma=suma+num
	print(suma)
print("")

tup=(1,2,3)
for _ in tup:
	print(_)
print("")

mylist=[(1,2,3,),(4,5,6),(7,8,9)]
for item in mylist:
	print(item)
print("")

# Tupple and Packing
mylist=[("c","d"),("e","f"),("g","h")]
for (a,b) in mylist:
	print(b)
print("")

d={"k1":1,"k2":2,"k3":3}
for item in d:
	print(item)			# this will only print thee key
print("")
for item in d.items():
	print(item)			# this will print both the item and the value

	












