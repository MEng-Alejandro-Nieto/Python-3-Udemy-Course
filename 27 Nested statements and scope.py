x=25
def printer():
	x=50
	return x
print(x)
print(printer())
print("")

'''
#							LEGB Rule
Local
Enclosing functions locals
Global
Built-in(python)
'''

# LOCAL
#lambda num: num**2

# Global
name= "this is a Global string"
def greet():
# Enclosing	
	#name ="Sammy"
	def hello():
# Local
		#name="michel"
		print("Hello "+name)
	hello()
print(greet())
print("")

x=50
def func(x):
	print(f"x is {x}")
	x=200
	print(f"I just changed x to {x}")
print(func(x))
print(x)
print("")

# if we want to set a variable as global we can do the following
x=10
def new_func(x):
	x=77
	return x
x=new_func(10)
print(x)













