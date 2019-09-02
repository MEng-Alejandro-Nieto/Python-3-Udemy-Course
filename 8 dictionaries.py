my_dict={"key1":"value1","key2":"value2"}					# creates a dictionary 
print(my_dict["key1"])										# prints the associated value of key1 

prices_lookup={"apple":2.99,"oranges":1.99,"milk":5.80}		# creates a dictionary 
print(prices_lookup['apple'])								# prints the associated value of apple

d={"k1":123,"k2":[0,1,2],"k3":{"inside key":100}}	# creates a dictionary of integers, lists, and dictionaries
print(d["k3"])										# prints the associated value of "k3"
print(d["k3"]["inside key"])						# prints the associated value of "k3" and the associated value of "inside key" which is inside
print(d["k2"][2])

a={"key1":["a","b","c"]}		# creates a dictionary 
print(a["key1"][2].upper())		# prints the associated value of "key1" and goes inside and choose the location 2 of the list and uppercase the letter "c"

d={"k1":100,"k2":200}			# creates a dictionary
print(d)
d["k3"]=300						#  adds a new key-value pair "k3":300
print(d)

d["k1"]="NEW VALUE"				# it replaces "k1":100 into "k1":"NEW VALUE"
print(d)

d={"k1":100,"k2":200}			# creates a dictionary

print(d.keys())					# it prints all the keys 
print(d.values())				# it prints all the values
print(d.items())				# it prints all the item pairs


