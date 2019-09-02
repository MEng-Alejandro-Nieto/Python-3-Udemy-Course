'''
1.  crear "baraja"
	generar "dinero"
	mezclar baraja
  	crear "mano jugador" 
  	crear "mano dealer"
	repartir 2 cartas a mano jugador y a mano delaer
	mostrar las dos cartas jugador y una carta dealer
		Bucle_1
		pedir carta jugador(s/n)?
			si "s":
				"mano jugador" quita carta a "baraja"
				verificar valor de mano
				bucle_2:
					si se pasa:
						FIN DEL DE JUEGO, GANA EL DEALER
					si no se pasa:

			si "n":
				fin del bucle_1

Bucle_3
		pedir carta jugador(s/n)?
			si "s":
				"mano dealer" quita carta a "baraja"
				verificar valor de mano
				bucle_2:
					si valor:
						FIN DEL DE JUEGO, GANA EL DEALER
					si no se pasa:

			si "n":
				fin del bucle_1


'''





import random

suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing=True


class Card():
	
	def __init__(self,suit,rank):
		self.suit=suit
		self.rank=rank
	
	def __str__(self):
		return self.rank + " of " +self.suit



class Deck():
	
	def __init__(self):
		self.deck=[]		# create an empty list
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp= ''
		for card in self.deck:
			deck_comp+='\n'+ card.__str__()
		return "the deck has: "+deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card=self.deck.pop()
		return single_card


class Hand:

	def __init__(self):
		self.cards=[]	# start with an empty list as we did in the Deck class
		self.value=0	# start with zero value
		self.aces=0		# add and atribute to keep track of aces

	def add_card(self,pulled_card):
		self.cards.append(pulled_card)
		self.value+=values[pulled_card.rank]

		if card.rank='Ace':
			self.aces+=1

	def adjust_for_ace(self):
		
		while self.value>21 and self.aces:
			self.value-=10
			self.aces-=1


class Chips():

	def __init__(self,total=100):
		self.total=total
		self.bet=0

	def win_bet(self):
		self.total+=self.bet

	def loose_bet(self):
		self.total-=self.bet


def take_bet(chips):
	
	while True:
		try:
			chips.bet=int(input("how many chips would you like to bet? "))
		except:
			print("sorry pleaseprovide a number")
		else:
			if chips.bet>chips.total:
				print(f"Not enough chip, you have {chips.total}")
			else:
				break

def  hit(deck,hand):
	single_card=deck.deal()
	hand.add_card(single.card)
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global Playing

	while True:
		x=input("hit or stand (h/s)? ")

		if x[0].lower()=="h":
			hit(deck,hand)
		elif x[0]=='s':
			print("Player stands Dealer's turn")
			playing= False
		else:
			print("sorry, I did not understand that, please enter h or s only")
			continue
		break	

def player_bust(player,dealer,chips):
	print("BUST PLAYER")
	chip.lose_bet()

def player_wins(player,dealer,chips):
	print("PLAYER WINS")
	chip.win_bet()


def dealer_bust(player,dealer,chips):
	print("PLAYER WINS, DEALER BUSTED")
	chip.win_bet()

def dealer_wins(player,dealer,chips):
	print("DEALER WINS")
	chip.loose_bet

def push(player,dealer,chips):
	print("Dealer and Player tie")


def take_bet(chips):
	while True
		try:
			chips.bet=int(input("How many chips would you like to bet? "))
		except:
			print("Sorry please provide an integer")
		else:
			if chips.bet>chips.total:
				print(f"Sorry, you do not have enough chips! you have {chips.total}")















test_deck=Deck()
test_deck.shuffle()
test_player=Hand()
pulled_card=test_deck.deal()
test_player.add_card(pulled_card)
print(pulled_card)
print(test_player.value)





