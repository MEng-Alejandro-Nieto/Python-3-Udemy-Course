'''
Python has decorators that allow you to track on extra 
functionality to an already existing function.

They use the @ operator and are then placed on top of
the original function 


'''

#---------------------------
print("1")
def func():
	return 1
print(func())
print("\n")
#---------------------------
print("2")
def hello():
	return "hello"
print(hello())
print("\n")
#---------------------------
print("3")
greet=hello
print(greet())
print("\n")
#---------------------------
print("4")
del hello
try:
	print(hello())
except:
	print("the hello function was deleted")
print("\n")
#---------------------------
print("5")
print(greet())
print("\n")
#---------------------------
print("6")
def hello(name='jose'):
	print("the hello() function has been executed")
print(hello())
print("\n")
#---------------------------
print("7")
def hello(name='jose'):
	print('the hello() function has been executed')

	def greet():
		return '\t this is the greet() function inside hello'
	print(greet())
print(hello())
print("\n")
#---------------------------
print("8")
def hello(name='jose'):
	print('the hello() function has been executed')

	def greet():
		return '\t this is the greet() function inside hello'
	
	def welcome():
		return "\t this is the welcome() inside hello" 
	
	print(greet())
	print(welcome())
	print("this is the end of the hello() function")
print(hello())
print("\n")
#---------------------------
print("9")
def Hello(name='jose'):
	print('the hello() function has been executed')

	def greet():
		return '\t this is the greet() function inside hello'
	
	def welcome():
		return "\t this is the welcome() inside hello" 

	print("I am going to return a function")
	if name=="jose":
		return greet
	else:
		return welcome
print(hello("jose"))
print("\n")
#---------------------------
print("10")
my_new_function=Hello()
print(my_new_function)
print("\n")
#---------------------------
print("11")
def cool():
	def super_cool():
		return 'I am super cool'
	return super_cool
some_func=cool()
print(some_func)
print("\n")
#---------------------------
print("12")
def cool():
	def super_cool():
		return 'I am super cool'
	return super_cool
some_func=cool()
print(some_func())
print("\n")
#----------------------------
print("13")
def other():
	return "this is second function"

def func(other):
	print("this will be printed for sure")
	print(other())
new=func(other)
print(new)
print("\n")
#----------------------------
print("14")

def new_decorator(original_func):
	def wrap_func():
		print("this is before the original function")

		print(original_func())

		print("this is after the original function")
	return wrap_func

def original_func():
	return "I want to be decorated"

decorator=new_decorator(original_func)
print(decorator())
print("\n")
#----------------------------
print("15")
@new_decorator			# this is and on/off function
def original_func():
	return "I want to be decorated"
print(original_func())
print("\n")
#----------------------------
print("16")
def original_func():
	return "I want to be decorated"
print(original_func())



























