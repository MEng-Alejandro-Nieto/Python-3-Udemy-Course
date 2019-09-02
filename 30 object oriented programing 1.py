class Lapiz:
	# ATRIBUTOS
	color= 'amarillo'			# ATRIBUTO 1
	contiene_borrador=False		# ATRIBUTO 2
	usa_grafito= True			# ATRIBUTO 3

	#METODOS
	def dibujar(self):
		print("el lapiz esta dibujando")

	def borrar(self):
		if self.contiene_borrador == True:
			print("el lapiz esta borrando")
		else:
			print("no puede borrar")

	def puede_borrar(self):
		return self.contiene_borrador

lapiz_generico= Lapiz()			# AGREGA LA CLASE "LAPIZ" AL OBJETO

lapiz_generico.color
lapiz_generico.dibujar()
lapiz_generico.borrar()
print(lapiz_generico.puede_borrar())# requiere de print para imprimir el return
# if we now say
lapiz_generico.contiene_borrador=True  # we change the atribute "contiene borrador" by doing this
lapiz_generico.borrar()




