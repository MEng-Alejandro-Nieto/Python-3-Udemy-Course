# write a function that computes the volume of a sphere given its radius

def vol(radius):
	volume=4/3*(3.14159)*radius**3
	return volume
print(vol(2))
print("")

# write a function that checks whether a number is in a given range
def check(num,low,high):
	return num >=low and num <=high
print(check(10,50,200))
print("")

# write a python function that accepts a string and calculate the number of uppercase
# letters and lower casse letters
def string(phrase):
	num_upper=0
	length= len("".join(phrase.split()))
	phrase="".join(phrase.split())
	for letter in phrase:
		if letter ==letter.upper():
			num_upper=num_upper+1
	print(f"the number of upper case letters is {num_upper}")
	print(f"the number of lower case letters is {length-num_upper}")
	print(phrase)
print(string("Hello Mr. Rogers, how are you this fine Tuesday"))
print("")

# write a python function that takes in a list and returns a new list with unique
# elements of the first list
def new_list(mylist):
	Set=set(mylist)
	new_list=list(Set)
	print(new_list)
print(new_list([1,1,1,1,2,2,2,2,3,3,3,3,4,4,5,6,6,7,4,]))
print("")

#write a python function that multiply all the numbers in a list
def multiplication(mylist):
	value=1
	for num in range(len(mylist)):
		value=value*mylist[num]
	print(f"{value}")
multiplication([1,2,3,4,5,5,5,-3])
print("")

# write a python function that checks wheter aa passed string
# is palindrome or not.
def pal(word):
	for num in range(len(word)):
		if word[num]==word[-(num+1)]:
			continue
		else:
			return False
	return True
print(pal("abagba"))
print("")







