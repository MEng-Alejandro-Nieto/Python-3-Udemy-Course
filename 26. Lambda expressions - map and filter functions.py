#								 MAP FUNCTION
def square(num):
	return num**2
my_nums=[1,2,3,4]
for item in map(square,my_nums):
	print(item)
print(list(map(square,my_nums)))


def splicer(mystring):
	if len(mystring)%2==0:
		return  "EVEN"
	else:
		return mystring[0]
names=["andy","nogal","firpo"]
print(list(map(splicer,names)))
	
#								 FILTER FUNCTION

def check_even(num):
	return num%2==0
mynums=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(check_even,mynums)))


#								Lambda Expression
# the idea is to create a temporary function that will be executed
# only one time, by doing this we save memory space
mynums=[12,13,14,15,16,17,18,19,20]
print(list(map(square,mynums))) # with map function
print(list(map(lambda num:num**2,mynums))) # with lambda expression

print(list(filter(check_even,mynums)))
print(list(filter(lambda check_even:check_even%2==0,mynums))) # with lambda expression










