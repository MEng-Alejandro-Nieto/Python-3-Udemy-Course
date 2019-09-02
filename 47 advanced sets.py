print("\nBlock 1\n")

s=set()
s.add(1)			# it adds 1 to the set
s.add(2)			# it adds 2 to the set	
s.add(2)			# as sets is a list of unique value it cannot add the 2 again
print(s)			# it prints the the set s		
s.clear()
print(s)
#---------------------------------
print("\nBlock 2\n")

s={1,2,3}
sc=s.copy()			# it creates a copy of s that is not modified if s is modified
l=s 				# it create a copy of s that is modified if s is modified
print(s)
print(sc)
s.add(10)
print(s)
print(sc)
print(l)
#---------------------------------
print("\nBlock 3\n")

print(s.difference(sc))
#---------------------------------
print("\nBlock 4\n")

s1={1,2,3}
s2={1,4,5}
s1.difference_update(s2)	# it removes all ellements in s1 that are in s2
print(s1)
#---------------------------------
print("\nBlock 5\n")

s={1,2,3,4,2,2,2}			
s.discard(2)				# it removes all 2 values from the set s
print(s)
#---------------------------------
print("\nBlock 6\n")

s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
print(s1.intersection(s2))	# it returns only the common values between s1 an s2
#---------------------------------
print("\nBlock 7\n")

print(s1)
s1.intersection_update(s2) # it leaves only the common values between s1 an s2 stored in s1
print(s1)					
#---------------------------------
print("\nBlock 8\n")
s1={1,2}
s2={1,2,4}
s3={5}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
#---------------------------------
print("\nBlock 9\n")
print(s1)
print(s2)
print(s1.issubset(s2))		# is s1 a subset of s2
print(s2.issubset(s1))		# is s2 a subset of s1
#---------------------------------
print("\nBlock 10\n")
print(s2.issuperset(s1))	# does s2 contains s1
#---------------------------------
print("\nBlock 11\n")
#---------------------------------
print("\nBlock 12\n")
s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
print(s1.symmetric_difference(s2))		# is returns the opposite of intersection
#---------------------------------
print(s1.union(s2))						# it returns the union of the s1 and s2 
#---------------------------------
print(s1)
s1.update(s2)							# it returns the union of the s1 and s2 and store it in s1
print(s1)
#---------------------------------
#---------------------------------
#---------------------------------
#---------------------------------
#---------------------------------
