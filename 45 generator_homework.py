'''
1. create a generator that generates the squares of numbers up to N
2. create a generator that yields "n" random numbers between a low and high numbers (inputs)
3. use iter() function to convert the string below into an interator
4. explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement
5. can you explain what gencomp is in the code below?


"
my_list=[1,2,3,4,5]
gencomp= (item for item in My_list if item>3)

for item in gencomp:
	print(item)
"

'''
#-----------------
print("Answer 1")
def squares(N):
	for num in range(N):
		yield num**2
g=squares(10)

for num in squares(10):
	print(num)
print("\n")
#-----------------
import random as rn
print("Answer 2")
def random(l,n,last):
	for num in range(last):
		yield rn.randint(l,n)
for num in random(1,10,3):
	print (num)
print("\n")
#-----------------
print("Answer 3")

s='hello'
s=iter(s)

print(next(s))








