a=1024
print(hex(a))
print(bin(a))
#--------------------------
b=5.23222
print(round(b,2))
#--------------------------
s="hellow how are you mary, are you feeling okay?"
contador=0
for letter in s:
	if letter==letter.lower():
		pass
	else:
		contador+=1
print(contador==0)
#--------------------------
s="twywywtwywbwhswwwwww"

contador=0
for letter in s:
	if letter.lower()=='w':
		contador+=1
print(contador)

#--------------------------
s1={2,3,1,5,6,8}
s2={3,1,7,5,6,8}
s=s1.symmetric_difference(s2)
t=s1.union(s2)
print(s)
print(t)
#--------------------------
b={x:x**3 for x in range(5)}
print(b)

#--------------------------
l=[1,2,3,4]
l.reverse()
print(l)
l.sort()
print(l)

