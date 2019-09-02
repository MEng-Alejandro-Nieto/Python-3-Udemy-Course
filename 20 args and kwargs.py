#						*args

def myfunc(a,b):
	# returns 5% of the sum of a and b
	return (a+b)*0.05
print(myfunc(60,40))

'''
the above  allow us to to define to values a and b however for varius parameters
we can use *args
'''

def myfunc(*args):
	return sum(args)*0.050
print(myfunc(10,10,10,10,10,10,10,10,10,10,10,10))
print("")

# or you can do

def myfunc(*args):
	for num in args:
		print (num)
print(myfunc(1,2,3,4,5,6))


#						** Kwargs


def myfunc(**kwargs):
	if "fruit" in kwargs:
		print("my fruit of choice is {}".format(kwargs["fruit"]))
	else:
		print("I did not find any fruit here")
print(myfunc(fruit="apple",name="alejandro"))
print("")

def myfunc(**kwargs):
	print(kwargs)
print(myfunc(name="alejandro", number=10, mylist=[1,2,3]))

#						COMBINED *args and **kwargs

def myfunc(*args, **kwargs):
	print("I would like {} {}".format(args[0], kwargs["food"]))
print(myfunc(10,20,30,fruit="orange",food="rize",animal="dog"))



















