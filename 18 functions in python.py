def name_function():
	'''
	DOCSTRING: information abot the function
	INPUT: no input...
	OUTPUT: Hello
	'''
	print("Hello")
# help(name_function)
print("")

def say_hello(name):
	print(f"hello {name}")
say_hello("alejandro")
print("")

#  we can do the following in case the user do not provide a name
# otherwise is gonna throw an error
def say_hello2(name="name"):
	print(f"hello {name}")
say_hello2()
print("")

def say_hello3(name="name"):
	return f"hello {name}"
result=say_hello3("alejo")
print(result)
print("")

def sum(n1,n2):
	return n1+n2
result=sum(12.5,13.5)
print(result)
print("")

# create a function that find out if the word dog is in a string 
def dog(mystring):
	if "dog" in mystring.lower():
		return True
	else:
		return False
a=dog("I love my dog")
print(a)
print("")

# or better
def dog(mystring):
	return "dog" in mystring.lower()
a=dog("I love my cat")
print(a)
print("")

'''
PIG LATIN
* if word starts with a vowel, add "ay" to end
* if word does not start with a vowel, put first letter at the end, ten add "ay"
*word----ordway
-apple---appleay
'''
def pig_latin(word):
	first_letter=word[0]
	if word[0] in "aeiou":
		newword=word+"ay"
		return newword
	else:
		newword=word[1:]+word[0]+"ay"
		return newword

print(pig_latin("apple"))




