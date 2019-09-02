x = 0
while  x < 5:
	print(f"the current vue is {x}")
	x=x+1
else:
	print("x is not less than 5")
print("")

# break: breaks out of the current closest enclosing loop
# continue: goes to the top of the closest enclosing loop
# pass: des nothing at all
x=[1,2,3]
for _ in x:
	pass
print("")

mystring="sammy"
for letter in mystring:
	if letter =="a":
		continue
	print(letter)
print("")

mystring="sammy"
for letter in mystring:
	if letter =="y":
		break
	print(letter)
print("")




