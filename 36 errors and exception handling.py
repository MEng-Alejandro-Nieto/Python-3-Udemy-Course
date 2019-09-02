'''
we use three keywords for this:
try: This is the block of code to be attempted (may lead to an error)
excpet: Block of code will execute in case there  is an error in try block
finally: a final block of code to be executed, regardless of an error.
'''
def add(n1,n2):
	print(n1+n2)
add(10,20)
'''
number1= 10
number2=input("please provide a number: ")
add(number1,nummber2)
the above code will lead to an error since number two is saved as
a string type variable, in here we can do the following
'''
'''
number1= 10
number2=input("please provide a number: ")
try:
	add(number1,number2)
except:
	print("there is an error in the try section")
finally:
	print("I always run")
'''

def ask_for_int():
	while True:
		try:
			result=int(input("please provide a number: "))
		except:
			print("Whoops! that is not a number")
		else:
			print("there is no error, 'good job'")
			break	
		finally:
			print("end of try/except/finally")

ask_for_int()









