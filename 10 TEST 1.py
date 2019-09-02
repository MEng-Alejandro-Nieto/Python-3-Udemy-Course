# write a brief description of all the following object types and data structures we  have learned about:

# Number: number can be of two different types, integers such as (1,  13,  300) or float such as (1.2,   35.159,   0,004)
# Strings: this is basically text that can be indexing or sliced
# List: a list is a colection of ordered elements, this elements can be integer, float, string or a list and they can be mutable or change
mylist=["Hello World",5,10.3, ["List",5]]
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
# Dictionaries: is a colection of unordered  elements that can be of any type, is similar to a list, but the difference is that the data inside is not tracked by a number but by a key  value 
mydictionary={"value 1":2,"value 2":"string","value 3":["Hello World",5,10.3, ["List",5]]}
print(mydictionary["value 1"])
print(mydictionary["value 2"])
print(mydictionary["value 3"])  
# Tuples: a tuple is the same as a list however these are immutable and are enclosed by curved brackets
mytuple= (1,"string",[2,3])
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])

# 														STRINGS
# Given the "Hello"  give and index command that returns "e".
name="Hello"
print(name[1])

# Reverse the string "Hello" using slicing:
reverse=name[::-1]
print(reverse)

# Given the string "Hello", give two methods of producing  the letter "o" using indexing.
print(name[-1])
print(name[4])
#														LISTS

# Build this list [0,0,0] two separate ways
mylist=[0,0,0]
a=[0]
newlist=a*3
print(mylist)
print(newlist)

#Reasign "Hello" in the folowing nested list to say "goodbye" instead
list3=[1,2,[3,4,"Hello"]]
list3[2][2]="goodbye"
print(list3)

# Sort the list below:
list4=[5,3,4,6,1]
list4.sort()
print(list4)

#														DICTIONARIES
# Use keys and indexing,grab the "hello" from the following dictionaries
d={"simple key":"hello"}
print(d["simple key"])
d={"k1":{"k2":"hello"}}
print(d["k1"]["k2"])
d={"k1":[{"nest_key":["this is deep",["hello"]]}]}
print(d["k1"][0]["nest_key"][1][0])

# can u sort a dictionary? a dictionary can be sort since by nature is unordered

#														TUPLES
# what is the major difference between a tuple and a list? the tuples are immutable
# how do you create a tuple?
mytuple=(1,["string",2.2],{"deep":2})
print(mytuple)


#														SETS
# what is unique about sets? a set is like a list of unique values
mylist=[1,1,9,8,6,6,2,4,7,6,7,3,6]
print(set(mylist))


#														BOOLEAN
print(1<2)		# 1 menor que 2?
print(1>2)		# 1 mayor que 2?
print(1==1)		# 1 igual a 1?
print(1==0)		# 1 igual a 0?
print(1!=1)		# 1 no es igual a 1?

# final question
# what is the boolean output of the cell block below?
one=[1,2,[3,4]]
two=[1,2,{"k1":4}]
a=one[2][0]>=two[2]["k1"]	# is this true or false?
print(f"this is {a}")

























