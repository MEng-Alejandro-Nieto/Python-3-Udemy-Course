# write a function called "myfunc" that prints the string "Hello World"
def myfunc():
	return print("Hello World")
myfunc()
print("")

# write a function called "myfunc" that takes in a Name, and prints "Hello Name"
def myfunc(Name):
	return print(f"Hello {Name}")
myfunc("alejandro")
print("")

# define a function called "myfunc" that takes in a bolean value 
#(True or False). if True return "Hello", and if False, Return "Goodbye"
def myfunc(a):
	if a=="True":
		return print("Good morning")
	else:
		return print("Goodbye")
myfunc("True")
print("")

#Define a function called myfunc that takes three arguments x,y,z. if z is True, return x, if z is false return y
def myfunc(x,y,z):
	if z=="True":
		return x 
	else:
		return y 
print(myfunc(1,2,"True"))
print("")

# Define a function called myfunc that takes in two arguments and returns  their sum
def myfunc(a=0,b=0):
	return a+b
print(myfunc(40,60))
print("")

# Define a function called is_even that takes in one argumet, and returns True if the passed-in value is even, False if it is not
def is_even(a):
	if a%2==0:
		return True
	else:
		return False
print(is_even(9))
print("")

# Define a function called "is_greater" that takes in two arguments, and returns True if the first value is greater than the second,
# False if it is less than or equal to the second.

def is_greater(a,b):
	if a>b:
		return True
	else:
		return False
print(is_greater(10,11))
print("")

#




















