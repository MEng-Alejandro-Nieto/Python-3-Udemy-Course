'''
PROBLEM 1
handle the exception thrown by the code bellow and except blocks

for i in ["a","b","c"]:
	print(i**2)
'''

for i in ["a","b","b"]:

	try:
		print(i**2)
	except:
		print("there is an error in above statement")




'''
PROBLEM 2

handle the exception thrown by the code bellow by using try and except
block, then use finally block to print "All Done"

x=5
y=0
z=x/y
'''
x=5
y=0
try:
	z=x/y
except:
	print("this is operation in not possible")
finally:
	print("All Done")



'''
PROBLEM 3

write a function that asks for an integer and prints the square of it, use 
a while loop with try, except, else block to account for incorrent inputs

def ask():
	pass
'''
def func(integer=0):
	while True:
		try:
			integer=int(input("insert the value: "))
		except:
			print("invalid value")
		else:
			print(f"good Job the value is {integer**2}")
			break
func()
	









