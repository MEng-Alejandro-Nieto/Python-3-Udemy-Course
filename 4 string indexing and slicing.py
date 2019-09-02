mystring="Hello World"
a=mystring[0]		# it will capture the letter or value located at the position 0 of the variable mystring (in this case "H")
b=mystring[4]		# it will capture the letter or value located at the position 4 of the variable mystring (in this case "o")
c=mystring[5]		# it will capture the letter or value located at the position 5 of the variable mystring (in this case " ")
print(mystring[0])
print(b)
print(c)
# NOW SLICING
d=mystring[0:7]			# it will capture the characters from the position 0 to 7 (but not included) each 1 position
e=mystring[3:7:1]		# it will capture the characters from the position 3 to 7 (but not included) each 1 position
f=mystring[1:11:2]		# it will capture the characters from the position 1 to 11 each 2 position
yourstring="animal"
g=yourstring[::-1]		# it will capture the character in an inverse position
h=yourstring[::-2]	# it will capture the character in an inverse position each two positions
print(d)
print(e)
print(f)
print(g)
print(h)
print('I love you mom'[5])





