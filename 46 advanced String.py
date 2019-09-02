s='hello world'
print(s)
print(s.capitalize())		# capitalize only the first letter
print(s.upper())			# capitalize all letters in the string
print(s.count('o')) 		# it counnts how many 'o' the string has
print(s.find('o'))			# it will print the first position of the letter passed in
print(s.center(20,'z'))		# the string is centered and surrounded by 'z'  in such a way that the total number of letter is 20
print("hola\tmama")			# '\t' it tabs the text
s='hello'
print(s.isalnum())			# are all alphanumeric ?
print(s.isalpha())			# are al alpha ?
print(s.isspace())			# there is a space?
print(s.istitle())			
print('HELLO'.isupper())	# it check if all characters are upppercase

s='Hello mom'
print(s.split('o'))			# it does it for all 'o'
print(s.partition('o'))		# it does it only for the first 'o'	


