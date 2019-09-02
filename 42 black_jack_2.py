'''
								OBJETOS
1. LA BARAJA
2. LA CARTA
3. LA MANO DEL JUGADOR
4. LA MANO DEL DEALER
5. BILLETERA (EL DINERO QUE TIENE EL JUGADOR PARA APOSTAR)

								FUNCIONES
1. crear la "BARAJA"
2. mezclar la "BARAJA"
3. pedir apuestas de la "BILLETERA"
4. repartir la carta a "MANO DEL JUGADOR" y "MANO DEL DEALER"
5. pedir si desea añadir "CARTA" a "LA MANO DEL JUGADOR"
		5.1 añadir "LA CARTA" a "LA MANO DEL JUGADOR"
		5.2 verificar que la suma de "LA MANO DEL JUGADOR" sea menor o igual a 21 
6. repartir "LA CARTA" a "LA MANO DEL DEALER"
	6.1 repetir hasta que el valor de "MANO JUGADOR" le gane a "LA MANO DEL DEALER" o se pase de 21


'''
import random

#----------------------------------------------------------

#----------------------------------------------------------
class La_baraja():
	numeros=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
	valores={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11,}
	
	def __init__(self):
		self.baraja=[]
		for num in range(4):
			for num in self.numeros:
				self.baraja.append(num)
	def mezclar(self):
		random.shuffle(self.baraja)
	def retirar_carta(self):
		return self.baraja.pop()	
	def imprimir(self):
		return self.baraja
#----------------------------------------------------------
class Mano_jugador():
	def __init__(self,maso):
		self.cartas_jugador=[]
	def recibir(self):
		self.cartas_jugador.append(maso.retirar_carta())
	def imprimir(self):
		return self.cartas_jugador
#----------------------------------------------------------
class Finanzas():
	
	def __init__(self,resultado,dinero,apuesta):
		self.resultado=resultado
		self.dinero=dinero
		self.apuesta=apuesta
	
	def sumar_quitar(self):
		if   self.resultado==1 or self.resultado==2:
			self.dinero=self.dinero-self.apuesta
		else:
			 self.dinero=self.dinero+self.apuesta
		return self.dinero

	def imprimir(self):
		if   self.resultado==1 or self.resultado==2:
			return f"Has perdido {self.apuesta} CAD"
		else:
			 return f"Has ganado {self.apuesta} CAD"
#----------------------------------------------------------

class Mano_dealer():

	def __init__(self,maso):
		self.cartas_dealer=[]
	def recibir(self):	
		self.cartas_dealer.append(maso.retirar_carta())
	def imprimir(self):
		return self.cartas_dealer
#----------------------------------------------------------
class Suma():
	
	def __init__(self,mano_dealer,mano_jugador,maso):
		self.mano_dealer=mano_dealer
		self.mano_jugador=mano_jugador
		self.maso=maso
	
	def valor_jugador(self):
		self.suma_jugador=0
		self.num_aj=0
		for num in self.mano_jugador:
			self.suma_jugador=self.suma_jugador+self.maso[num]
			if num =="A":
				self.num_aj+=1
		if self.suma_jugador>21 and self.num_aj>0 : # si se pasa y tiene "A" en la mano
			while self.num_aj>0:
				self.suma_jugador-=10
				self.num_aj-=1
				if self.suma_jugador<=21:
					break
		return self.suma_jugador

	def valor_dealer(self):
		self.suma_dealer=0
		self.num_ad=0
		for num in self.mano_dealer:
			self.suma_dealer=self.suma_dealer+self.maso[num]
			if num =="A":
				self.num_ad+=1
		if self.suma_dealer>21 and self.num_ad>0 : # si se pasa y tiene "A" en la mano
			while self.num_ad>0:
				self.suma_dealer-=10
				self.num_ad-=1
				if self.suma_dealer<=21:
					break
		return self.suma_dealer
#----------------------------------------------------------
def pregunta_jugador():
	while True:
		try:
			pregunta=input("desea tomar carta (Y/N) ? ")
		except:
	 		print("valor numerico no es reconocido, porfavor ingrese 'Y' para tomar carta o 'N' para plantarse")
		else:
			if pregunta.lower()=="y":
				global_player=True
				break
			elif pregunta.lower()=="n":
 				global_player=False
 				break
			else:
 				print("valor no reconocido ")
	return global_player
#----------------------------------------------------------
class Se_pasa():

	def __init__(self,valor_jugador):
		self.valor_jugador=valor_jugador

	def se_paso(self):
		if self.valor_jugador>21:
			self.player_bust=True
			return self.player_bust
		else:
			self.player_bust=False
			return self.player_bust

	def resultado(self):
		if self.player_bust==True:
			self.resultado=1 					# El jugador se pasa de 21 y gana el dealer
			return self.resultado
#----------------------------------------------------------
class Quien_gana():

	def __init__(self,resultado,valor_jugador,valor_dealer,mano_jugador,mano_dealer):
		self.resultado=resultado
		self.valor_jugador=valor_jugador
		self.valor_dealer=valor_dealer
		self.mano_jugador=mano_jugador
		self.mano_dealer=mano_dealer

	def imprimir(self):
		if   self.resultado==1:
			return f"\n\nMANO JUGADOR: {self.mano_jugador.imprimir()}\nMANO DEALER:  {self.mano_dealer.imprimir()}\nEl jugador se pasa con {self.valor_jugador}, el dealer gana con {self.valor_dealer} "
		elif self.resultado==2:
			return f"\n\nMANO JUGADOR: {self.mano_jugador.imprimir()}\nMANO DEALER:  {self.mano_dealer.imprimir()}\nEl dealer gana con {self.valor_dealer},  el jugador pierde con {self.valor_jugador} "
		elif self.resultado==3:
			return f"\n\nMANO JUGADOR: {self.mano_jugador.imprimir()}\nMANO DEALER:  {self.mano_dealer.imprimir()}\nEl jugador gana con {self.valor_jugador}, el dealer se pasa con {self.valor_dealer}"
#----------------------------------------------------------
def Seguir():
	continuar=input("Desea continuar (Y/N) ? ")
	while True:
		
		if continuar.lower()=="y" or continuar.lower()=="n" :
			break
		else:
			continuar=input(print("El valor ingresado no se entiende, por favor ingrese 'Y' or 'N'"))
	if continuar.lower()=="y":
		return "continuar"
	else:
		return"retirarse"
#----------------------------------------------------------
print("\n"*100)
while True:
	try:
		dinero=int(input("Cuantas fichas desea comprar? "))
	except:
		print("\n"*100)
		print("Ingrese unicamente valores numericos")
	else:
		break
print("\n"*100)
#----------------------------------------------------------
while True:

	while True:
		try:
			print(f"Tu dinero: {dinero}")
			apuesta=int(input("Cuanto apuesta? "))
		except:
			print("\n"*100)
			print("Ingrese unicamente valores numericos")
			print("\n")
		else:
			if apuesta>dinero:
				print("\n"*100)
				print("No tienes suficiente dinero")
				print("\n")
			else:
				break
	print("\n"*100)
	maso=La_baraja()					# Crear la baraja
	maso.mezclar()						# Mezclar la baraja
	mano_jugador=Mano_jugador(maso)		# Crear  mano jugador
	mano_jugador.recibir()				# Mano jugador toma carta
	mano_dealer=Mano_dealer(maso)		# Crear mano dealer
	mano_dealer.recibir()				# Mano dealer toma carta
	mano_jugador.recibir()				# Mano jugador toma carta
	mano_dealer.recibir()				# Mano dealer toma carta
	suma=Suma(mano_dealer.imprimir(),mano_jugador.imprimir(),maso.valores)	# Crea objeto para calcular las manos
	suma.valor_jugador()				# Calcula la mano del jugador
	suma.valor_dealer()					# Calcula la mano del dealer
	print("\n"*100)
	print(f"Tu dinero:  {dinero}")
	print(f"Tu apuesta: {apuesta }\n")
	print(f"la mano del jugador es {mano_jugador.imprimir()} y vale {suma.valor_jugador()}")
	print(f"la mano del dealer es  [{mano_dealer.imprimir()[0]} ?]")

	while True:
		global_player=pregunta_jugador()
		if global_player:
			mano_jugador.recibir()
			suma=Suma(mano_dealer.imprimir(),mano_jugador.imprimir(),maso.valores)
			suma.valor_dealer()
			suma.valor_jugador()
			print("\n"*100)
			print(f"Tu dinero:  {dinero}")
			print(f"Tu apuesta: {apuesta }\n")
			print(f"la mano del jugador es {mano_jugador.imprimir()} y vale {suma.valor_jugador()}")
			print(f"la mano del dealer es  [{mano_dealer.imprimir()[0]} ?] y vale {suma.valor_dealer()}")
			se_pasa=Se_pasa(suma.valor_jugador())
			player_bust=se_pasa.se_paso()
			if se_pasa.se_paso():
				resultado=se_pasa.resultado()
				break
		else:
			player_bust= False
			break
	print("\n"*100)
	if player_bust== False:
		while True:
				if 	suma.valor_dealer()>suma.valor_jugador() and suma.valor_dealer()<= 21:
					resultado=2				# el dealer gana
					break
				mano_dealer.recibir()
				suma=Suma(mano_dealer.imprimir(),mano_jugador.imprimir(),maso.valores)
				suma.valor_dealer()
				suma.valor_jugador()
				if 	suma.valor_dealer()>suma.valor_jugador() and suma.valor_dealer()<= 21:
					resultado=2				# el dealer gana
					break
				elif suma.valor_dealer()>21:
					resultado=3				# El dealer se pasa de 21 y gana el jugador
					break
	valor_jugador=suma.valor_jugador()
	valor_dealer=suma.valor_dealer()
	finanzas=Finanzas(resultado,dinero,apuesta)
	quien_gana=Quien_gana(resultado,valor_jugador,valor_dealer,mano_jugador,mano_dealer)
	dinero=finanzas.sumar_quitar()
	print(quien_gana.imprimir())
	print(dinero)
	if dinero==0:
		print("TE HAS QUEDADO SIN DINERO, ADIOS")
		break
	seguir=Seguir()

	if seguir=="continuar":
		seguir==True
	else:
		print("\n"*100)
		print(f"TE RETIRAS CON {dinero}, ADIOS")
		break





