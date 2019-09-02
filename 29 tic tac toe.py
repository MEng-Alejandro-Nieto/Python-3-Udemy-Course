a=[" "]*10; condition=True; position=0; num=0

# PRINTS THE BOARD
def board(a):
	print("\n"*100)
	print("      |     |     ")
	print(f"   {a[7]}  |  {a[8]}  |  {a[9]}  ")
	print("      |     |     ")
	print("- - - - - - - - - - ")
	print("      |     |     ")
	print(f"   {a[4]}  |  {a[5]}  |  {a[6]}  ")
	print("      |     |     ")
	print("- - - - - - - - - - ")
	print("      |     |     ")
	print(f"   {a[1]}  |  {a[2]}  |  {a[3]}  ")
	print("      |     |     ")

# DEFINE IF PLAYER ONE IS "X" OR "O"
def exorcircle():
	simbol=[0,0]
	verificator=True
	while verificator:
		player1=input("PLAYER 1 WANTS TO BE 'x' (Y/N)? ").lower()
		if player1=="y":
			simbol=["x","o"]
			verificator=False
		elif player1=="n":
			simbol=["o","x"]
			verificator=False
		else:
			print("\nOPTION INVALID\n")
	return simbol
simbol=exorcircle()

# DEFINE THE CONDITIONS TO WIN THE MATCH
def winner(position,condition,num):
	if position==1:
		if (a[1]==a[2]==a[3]) or (a[1]==a[4]==a[7]) or (a[1]==a[5]==a[9]):
			condition=False
	elif position==2:
		if (a[2]==a[1]==a[3]) or (a[2]==a[5]==a[8]):
			condition=False
	elif position==3:
		if (a[3]==a[1]==a[2]) or (a[3]==a[6]==a[9]) or (a[3]==a[5]==a[7]):
			condition=False
	elif position==4:
		if (a[4]==a[5]==a[6]) or (a[4]==a[1]==a[7]):
			condition=False
	elif position==5:
		if (a[5]==a[4]==a[6]) or (a[5]==a[2]==a[8]):
			condition=False
	elif position==6:
		if (a[6]==a[4]==a[5]) or (a[6]==a[3]==a[9]):
			condition=False
	elif position==7:
		if (a[7]==a[8]==a[9]) or (a[7]==a[1]==a[4]) or (a[7]==a[5]==a[3]):
			condition=False
	elif position==8:
		if (a[8]==a[7]==a[9]) or (a[8]==a[5]==a[2]):
			condition=False
	elif position==9:
		if (a[9]==a[7]==a[8]) or (a[9]==a[6]==a[3]) or (a[9]==a[5]==a[1]):
			condition=False
	if condition== False:
		return condition

# insert "x" or "o" in the board and determine who wins
def play():
	global a
	condition=True; num=2;board(a)	
	while condition==True:
		position=int(input(f"PLAYER {num%2+1} SELECT POSITION: "))
		if a[position]==" ":
			a[position]=simbol[num%2]
			board(a)
			winner(position,condition,num)
			if winner(position,condition,num)==False:
				answer=input(f"PLAYER {num%2+1} IS THE WINNER,DO YOU WANT TO PLAY AGAIN (Y/N) ? ")
				if answer.lower()=="y":
					a=[" "]*10; condition=True; position=0; num=0
					play()
					condition=False
				elif answer.lower()=="n":
					print("GOOD BYE :)")
					condition=False
				else:
					print("INVALID OPTION")
			num+=1
			if num==11:
				print("TIE GAME\n\n")
				answer=input("DO YOU WANT TO PLAY AGAIN (Y/N) ? ")
				if answer.lower()=="y":
					a=[" "]*10; condition=True; position=0; num=0
					play()
					condition=False				
				elif answer.lower()=="n":
					print("GOOD BYE :)")
					condition=False
					break
				else:
					print("INVALID OPTION")
		else:
			print("THIS POSITION IS NOT EMPTY")
play()



