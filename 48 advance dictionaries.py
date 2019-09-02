#---------------------
print("\nBlock 1\n")
d={'k1':1,'k2':1,'k3':3,'k4':4,'k5':5}

#---------------------
print("\nBlock 2\n")
a={x:x**3 for x in range(4)}		# dictionary comprehension
print(a)

#---------------------
print("\nBlock 3\n")
a={k:v**3 for k,v in zip(['a','b','c','d','e','f'],range(6))}		# dictionary comprehension
print(a)

#---------------------
print("\nBlock 4\n")
d={'k1':1,'k2':1,'k3':3,'k4':4,'k5':5}
for k in d:
	print (k)
#---------------------
print("\nBlock 5\n")
for k in d.values():
	print (k)
#---------------------
print("\nBlock 6\n")
for k in d.items():
	print (k)
#---------------------
print("\nBlock 7\n")
print(list(d))
#---------------------
print("\nBlock 8\n")
print(list(d.items()))
#---------------------
print("\nBlock 9\n")
print(list(d.values()))






