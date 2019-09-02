my_list2=[1,2,3]						# a list only of integers
my_list=["STRING",100,23.2]				# a list mixed of string, integers and float values
a=len(my_list)							# assign to a the length of a list
print(f"the length of my_list is {a}")	# print the value of a which is the length of "my_list"
b=my_list[0]							# assign to b the value at the position 0 of the variable "my_list"
print(b)								# prints the vaue of b	THIS IS INDEXING
c=my_list[1:]							# it assigns the value from position 1 to the end of "my_list"
print(c)								

# CONCATENATION
my_list=["one","two","three"]
another_list=["four","five"]
new_list=my_list+another_list			# concatenate my_list and another_list
print(new_list)

# MUTATE OR CHANGING A LIST
new_list[0]="STRING"					# It changes the position 0 of the  list called "new_list"
print(new_list)

#ADD ELEMENTS TO A LIST
new_list.append("six")					# it adds a element at the end of location of the list
new_list.append("seven")
print(new_list)

# SUBSTRACT ELEMENTS
a=new_list.pop()						# it removes the last element of a list and assign it to a
print(a)
print(new_list)
b=new_list.pop(0)						# it removes the first element of the list and assign it to b
print(b)
print(new_list)

# SORT
new_list=["a","e","x","b","c"]
num_list=[4,1,8,3]
new_list.sort()							# it will sort new_list in alphabetic order
num_list.sort()							# it will sort num_list in numercal order
print(new_list)
print(num_list)

new_list=[7,8,9,4,5,6,1,2,3]
my_sorted_list=new_list.sort()			# this wil not work since sort() occurs in place
print(my_sorted_list)					# this wil not work since sort() occurs in place
new_list=[7,8,9,4,5,6,1,2,3]

new_list.sort()							# it sorts new_list
my_sorted_list=new_list					# then assign the values to "my_sorted_list"
print(my_sorted_list)					# the prints it

# REVERSE
new_list.reverse()						# it reverses the order of the values in the list
print(new_list)



