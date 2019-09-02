#define a function that returns the lesser of two given numbers if both are even
# but returns the greater if one or both are odd
def func(a,b):
	if a%2==0 and b%2==0:
		return min(a,b)
	else:
		return max(a,b)
print(func(12,21))	# should return 21
print(func(12,10))	# should return 10
print("")

# write a function that takes a two word string and returns true if both words
# begin with same letter or false in other case
def func(words):
	words=words.lower().split()
	return words[0][0]==words[1][0]
print(func("animal Adilla"))
print("")

# define a function  that takes in two integers, returns true if the sum of the integer is 20 or
# if one of the integers is 20. If not return false
def func(a,b):
	return a+b==20 or a==20 or b==20
print(func(20,1))



















