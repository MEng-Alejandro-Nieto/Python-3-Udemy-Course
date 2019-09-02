# USE for, split(), TO CREATE A STATEMENT THAT WILL PRINT OUT WORDS THAT START WITH "S"
#"print only the words that start with s in this statement"
sentence="print only the words that start with s in this statement"
sentence=sentence.split()
print(sentence)
for word in sentence:
	if word[0]=="s":
		print(word)
print("")

# USE RANGE TO PRINT ALL THE EVEN NUMBERS FROM 0 TO 10
for num in range(11):
	if num%2==0:
		print(num)
print("")

# USE A LIST COMPREHENSION TO CREATE A LIST OF ALL NUMBERS BETWEEN 1 AND 50 THAT ARE DIVISIBLE BY 3
mylist=[]
for num in range(50):
	if num%3==0:
		mylist.append(num)
print(mylist)
print("")

# GO THROUGH THE STRING BELOW AND IF THE LENGTH OF A WORD IS EVEN PRINT "even"
# "print every word in this sentence that has an even number of letters"
mylist="print every word in this sentence that has an even number of letters"
mylist=mylist.split()
for letter in mylist:
	length=len(letter)
	if length%2==0:
		print(f"the word {letter} is even")
	else:
		print(f"the word {letter} is odd")
print("")

# WRITE A PROGRAM THAT PRINTS THE INTEGERS FROM 1 TO 100. BUT FOR
# MULTIPLES OF THREE PRINTS "Fizz" INSTEAD OF THE NUMBER, AND FOR 
# THE MULTIPLES OF FIVE PRINT "Buss". FOR NUMBER WHICH ARE MULTIPLES
# OF BOTH THREE AND FIVE PRINTS "FizzBuzz"

for num in range(101):
	if num%3==0 and num%5==0:
		print("FizzBuzz")
	elif num%5==0:
		print("Buzz")
	elif num%3==0:
		print("Fizz")
	else:
		print(num)

# USE LIST COMPREHENSION TO CREATE A LIST OF THE FIRST LETTERS
# OF EVERY SINGLE STRING BELLOW
#"Create a list of the first letters of every word in this string"

sentence="Create a list of the first letters of every word in this string"
sentence=sentence.split()
mylist=[]
for letter in sentence:
	mylist.append(letter[0])
print(mylist)




















