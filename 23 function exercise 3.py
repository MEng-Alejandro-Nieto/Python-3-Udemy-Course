# OLD MACDONALD: write a function that capitalizes the first and fourth letters of a name
def old_macdonald(word):
	new=""
	if len(word)>=4:
		for num in range(len(word)):
			if num==0 or num==3:
				new=new+word[num].upper()
			else:
				new=new+word[num].lower()
	else:
		return print("The world has less than 4 letters")			
	return new
print(old_macdonald("macdonald"))
print("")
#OR
def old_macdonald(word):
	first=word[:3]
	second=word[3:]
	return first.capitalize()+second.capitalize()
print(old_macdonald("macdonald"))

#MASTER YODA: given a sentence, return a sentence with the words reversed
# "I am home"-----"home am I"
def master_yoda(sentence):
	new=""
	sentence=sentence.split()
	for num in range(len(sentence)):
		new=new+sentence[len(sentence)-num-1]
		new=new+" "
	return new
print(master_yoda("los amo a todos"))
# OR
def master_yoda(sentence):
	new=""
	sentence=sentence.split()
	sentence=sentence[::-1]
	return " ".join(sentence)
print(master_yoda("los amo a todos"))

# ALMOST THERE: given an integer n, return true if n is within 10 of either
# 100 or 200
def almost_there(num):
	return (abs(num-100)<= 10) or (abs(num-200)<=10)
print(almost_there(89))














