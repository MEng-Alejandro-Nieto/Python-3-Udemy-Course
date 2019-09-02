# SPY GAME: write a function that takes in a list of integers 
# and returns True if it contains 007 in order.

def spy_game(mylist):
	for num in range(len(mylist)-2):
		if mylist[num]==0 and mylist[num+1]==0 and mylist[num+2]==7:
			return True
	return False		
print(spy_game([0,0,7]))
print("")

# COUNT PRIMES: write a function that returns the number
# of prime numbers that exist up to and including a given number

def count_primes(value):
	count=0
	store=[2,3,5,7]
	if value<2:
		return 0
	elif value==2:
		print([2])
		return 1
	elif value==3 or value==4 :
		print([2,3])
		return 2
	elif value==5 or value==6:
		print([2,3,5])
		return 3
	else:
		num=2
		while num <= value:
			if num%2==0 or num%3==0 or num%5==0 or num%7==0:
				pass
				num=num+1
			else:
				count=count+1
				store.append(num)
				num=num+1
		print(store)
		return count+4
print(count_primes(10))











