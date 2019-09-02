'''
*generators function will automatically suspend and resume their execution
 and state around the last point value generation
* the advantage is that instead of having to compute an entire series of values up front,
the generator computes one value waits until the next value is called for
'''

#---------------------------------------------------------------------

print("Block 1")
# "create_cubes" will create a list of cubbes from 0 to "N"
def create_cubes(n):
	list_cubes=[]
	for num in range(n):
		list_cubes.append(num**3)

	return list_cubes
list_of_cubes=create_cubes(10)

for x in list_of_cubes:
	print(x)
print("\n")
# by doing the above the the memory will be ocupied with a list of number while
# the for lopp o printing them

#---------------------------------------------------------------------

print("Block 2")
def create_cubes(n):
	for num in range(n):
		yield num**3

print(f"{create_cubes(10)}\nas you can see, it only shows that you have a generator\nobject at this location memory")
for x in create_cubes(10):
	print(x)
print("\n")

#by doing this the numbers in "create_cubes" are being generating as they are called
# and so making the code more efficient

#---------------------------------------------------------------------

print("Block 3")
# lets do now the same with a fibonacci sequence (1,2,3,5,8,13...)
def fibonacci(n):
	a=1
	b=2
	for num in range(n) :

		if num==0:
			yield a
		elif num==1:
			yield b
		else:
			num=a+b; a=b; b=num
			yield num
for i in fibonacci(10):
	print(i)
print("\n")

#---------------------------------------------------------------------

print("Block 4")

def simple_gen():
	for x in range(3):
		yield x

for x in simple_gen():
	print (x)

g=simple_gen()
print("\n")
print(next(g))
print(next(g))
print(next(g))
print("\n")

#---------------------------------------------------------------------

print("Block 5")

s='hello'

for letter in s:
	print (letter)
#next(s) this will give a error, to iterate "s" we must do

s_iter=iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
