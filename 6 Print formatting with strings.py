#	1 METHOD --- .format()
print("his name is {}".format("Alejandro"))								# It will print "his name is Alejandro"
print("the next 3 words are {} {} {}".format('fox','brown','quick'))	# It will print "the next 3 words are fox brown quick"
print("the next 3 words are {2} {1} {0}".format('fox','brown','quick'))	# It will print "the next 3 words are  quick brown fox"
print("the next 3 words are {c} {a} {b}".format(a='fox',b='brown',c='quick'))	# It will print "the next 3 words are  quick brown fox"
a=1;  b=2;  c=a+b;	
print("the sum of {} + {} is equal to {}".format(a,b,c) )			# it will print "the sum of 1 + 2 is equal to 3"   
print("the result of {2} - {1} is equal to {0}".format(a,b,c))		# it will print "the result of 3 - 2 is equal to 1"
		# float formatting 
result=100/777
print("the result is {}".format(result))
print("the result is {r:10.3f}".format(r=result))					# It will print with a precision of 3 decimals and 10 spaces

#	2 METHOD --- f-strings
name = "Alejandro"
c=100
d=777
e=c/d
print(f"his name is {name}")										# It will print "his name is Alejandro"
print(f"the sum of {a}+{b}={c}")									# it will print "the sum of 1 + 2 is equal to 3"  
print(f"the resul of {c}/{d} ={e:10.5f}")							# It will print with a precision of 3 decimals and 10 spaces
