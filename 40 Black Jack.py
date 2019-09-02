import random
chips=100

class Black_Jack():

	hand_player=[]
	hand_dealer=[]

	def __init__(self,chips):
		self.chips=chips
		self.card_number=["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K"]
		random.shuffle(self.card_number)
		print(self.card_number)
		
	def bet(self):
		while True:
			try:
				self.bet=int(input("WHAT IS YOUR BET ? "))
				if self.bet<=self.chips:
					break
				else:
					print("Not enough chips")
			except:
				print("Only numeric characters ")


	def giving_cards(self):
		self.hand_player.append(self.card_number.pop())
		self.hand_dealer.append(self.card_number.pop())
		self.hand_player.append(self.card_number.pop())
		self.hand_dealer.append(self.card_number.pop())

		print(self.hand_player)
		print(self.hand_dealer)

	def defining_values(self):
		num=0
		self.jugador=[]
		while num <= (len(self.hand_player)-1):
			if (self.hand_player[num]=="J") or (self.hand_player[num]=="Q") or (self.hand_player[num]=="K"):
				self.jugador.append(10)
			elif self.hand_player[num]=="A":
				self.jugador.append(11)
			else:
				self.jugador.append(self.hand_player[num])
			num+=1
		num=0
		self.dealer=[]
		while num <= (len(self.hand_player)-1):
			if (self.hand_dealer[num]=="J") or (self.hand_dealer[num]=="Q") or (self.hand_dealer[num]=="K"):
				self.dealer.append(10)
			elif self.hand_dealer[num]=="A":
				self.dealer.append(11)
			else:
				self.dealer.append(self.hand_dealer[num])
			num+=1
		self.sum_jugador=sum(self.jugador)	
		self.sum_dealer=sum(self.dealer)
		print("\n"*100)
		print(f" JUGADOR:  {self.hand_player}")
		print(f" DEALER:   [{self.hand_dealer[0]},?]")

	def Turno_jugador(self):
		while True:
			self.take_player=input("Do you want to take another card (Y/N) ? ")
			if self.take_player.lower()=="y":
				self.hand_player.append(self.card_number.pop())
				self.jugador.append(self.hand_player[-1])
			else:
				break 
			self.contador=0
			for check_A in self.hand_player:
				if check_A=="A":
					self.contador+=1
			num=0
			self.jugador=[]
			while num <= (len(self.hand_player)-1):
				if (self.hand_player[num]=="J") or (self.hand_player[num]=="Q") or (self.hand_player[num]=="K"):
					self.jugador.append(10)
				elif self.hand_player[num]=="A":
					self.jugador.append(11)
				else:
					self.jugador.append(self.hand_player[num])
				num+=1
			self.sum_jugador=sum(self.jugador)
			if self.sum_jugador>21:
				print(self.sum_jugador)	
				if self.contador>0:
					for num in range(self.contador):
						self.sum_jugador=self.sum_jugador-10
						if self.sum_jugador<21:
							num=self.contador
					if self.sum_jugador>21:
						print("\n"*100)
						print(f" JUGADOR:  {self.hand_player}")
						print(f" DEALER:   {self.hand_dealer}")
						print(f" (1) player BUST with {self.sum_jugador}, dealer wins with {self.sum_dealer}")
						self.win=False
						break	
				else:
					print("\n"*100)
					print(f" JUGADOR:  {self.hand_player}")
					print(f" DEALER:   {self.hand_dealer}")
					print(f"(2) player BUST with {self.sum_jugador}, dealer wins with {self.sum_dealer}")
					self.win=False
					break
			print("\n"*100)
			print(f" JUGADOR:  {self.hand_player}")
			print(f" DEALER:   [{self.hand_dealer[0]},?]")

	def Turno_dealer(self):
		while True:
			if self.sum_jugador>21:
				break

			elif (self.sum_dealer > self.sum_jugador) and (self.sum_dealer<=21):
				#print("\n"*100)
				print(self.hand_player)
				print(self.hand_dealer)
				print(f"(3) dealer wins con {self.sum_dealer}")
				self.win=False
				break

			self.hand_dealer.append(self.card_number.pop())
			
			if (self.hand_dealer[-1]=="J") or (self.hand_dealer[-1]=="Q") or (self.hand_dealer[-1]=="K"):
				self.dealer.append(10)
			elif self.hand_dealer[-1]=="A":
				self.dealer.append(11)
			else:
				self.dealer.append(self.hand_dealer[-1])
			self.sum_dealer=sum(self.dealer)
			
			if (self.sum_dealer<=21) and (self.sum_dealer>self.sum_jugador):
				print("\n"*100)
				print(f" JUGADOR:  {self.hand_player}")
				print(f" DEALER:   {self.hand_dealer}")				
				print(f"(4) dealer wins with {self.sum_dealer}")
				self.win=False
				break
			elif self.sum_dealer > 21:
				if "A" in self.hand_dealer:
					for num in range(len(self.hand_dealer)):
						if self.hand_dealer[num]=="A":
							self.sum_dealer=self.sum_dealer-10
							if (self.sum_dealer<=21) and (self.sum_dealer>self.sum_jugador):
								print("\n"*100)
								print(f" JUGADOR:  {self.hand_player}")
								print(f" DEALER:   {self.hand_dealer}")				
								print(f"(5) dealer wins with {self.sum_dealer}")
								self.win=False
								break
					if self.sum_dealer>21:
						print("\n"*100)
						print(f" JUGADOR:  {self.hand_player}")
						print(f" DEALER:   {self.hand_dealer}")
						print(f"(6) dealer BUST with {self.sum_dealer}, player wins with {self.sum_jugador}")
						self.win=True
						break
				else:
					print("\n"*100)
					print(f" JUGADOR:  {self.hand_player}")
					print(f" DEALER:   {self.hand_dealer}")
					print(f"(7) dealer BUST with {self.sum_dealer}, player wins with {self.sum_jugador}")
					self.win=True
					break

			elif self.sum_dealer==self.sum_jugador:
				print("\n"*100)	
				print(f" JUGADOR:  {self.hand_player}")
				print(f" DEALER:   {self.hand_dealer}")
				print(f"(8) TIE GAME")
				self.win=0
				break
	def new_chips(self):
		if self.win==False:
			self.chips=self.chips-self.bet
		elif self.win==True:
			self.chips=self.chips+self.bet
		print(f"your new balance is {self.chips}")
		

condition=True
while condition:
	game=Black_Jack(chips)
	game.bet()
	game.giving_cards()
	game.defining_values()
	game.Turno_jugador()
	game.Turno_dealer()
	game.new_chips()

	while True:
		try:	
			repeat=input("You want to play again (Y/N)  :")
			if repeat.lower()=="y":
				self.hand_player=[]
				self.hand_dealer=[]
				break
			elif repeat.lower()=="n":
				condition=False
				break
		except:
			print("Ups there is an error in your input")






























