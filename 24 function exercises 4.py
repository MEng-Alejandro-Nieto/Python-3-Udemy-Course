#  FIND 33: write a function that return True if a given list
# contains a 3 next to a 3 somewhere
def has_33(args):
	for element in range(0,len(args)-1):
		if args[element]==3 and args[element+1]==3:
			return True
	return False
print(has_33([1,2,4,4,4,4,]))
print("")

# PAPER  DOLL: given a string, return a string where for every character in the original
# there are three characters
def paper_doll(word):
	new=""
	for letter in word:
		new=new+3*letter
	return new
print(paper_doll("ohh"))

# BLACKJACK: given three integers between 1 and 11, if their sume is
# less than or equal to 21, return their sum. If their sm exceeds
# 21 and there is an eleven, reduce the total sum by 10. finally if the sum
# even after adjustments exceeds 21 return "BUST"

def black_jack(a,b,c):
	suma= a+b+c
	if a==11 or b==11 or c==11:
		if suma-10 <= 21:
			return a+b+c-10
		else:
			return "BUST"
	elif suma<=21:
		return a+b+c
	else:
		return "BUST"
print(black_jack(11,11,10))
print("")

# SUMMER OF 69: return the sum of the numbers in the array, except
# ignore sections of numbers starting with a 6 and extending to the 
# next 9 

def summer_69(a):
	i=0;
	if 6 in a and 9 in a:
		for num in a:
			if num==6:
				b=i
				i=i+1
			elif num==9:
				c=i
				i=i+1
			else:
				i=i+1
		if b<c:
			return sum(a[:b]+a[c+1:])
		else:
			sum(a)
	else:
		return sum(a)
print(summer_69([1,3,5,6,8,9,10]))
	














