# define a funcion called "myfunc" that takes in an arbitrary number od arguments, and returns the sum of those arguments
def myfunc(*args):
	return sum(args)
print(myfunc(1,2,3,4,5))
print("")


# define a function called myfunc that takes in an arbitrary number of
# arguments, and returns a lists containing only those arguments that are even
mylist=[]
def myfunc(*args):
	for num in args:
		if num%2==0:
			mylist.append(num)
	return mylist
print(myfunc(1,2,3,4,5,6,7,8,10))
print("")

# Define a function called myfunc that takes in a string, and returns 
# a matching string every even letter is uppercase and every odd letter is lower case.
# assume that the incoming string only contains letters, and do not worry about spaces
# or punctuation. the output string can start with either and uppercase or lowercase 
# letter, so long as letters alternate throughout the string


def myfunc(word):
	new=""
	for num in range(len(word)):
		if num%2==0:
			new=new+word[num].upper()
		else:
			new=new+word[num].lower()

	return new

print(myfunc("holatodos"))


