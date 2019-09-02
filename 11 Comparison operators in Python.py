#	==		equality
#	!=		not equality
#	>		greater than
#	<		less than
#	>= 		greater or equal to
#	<=		less or equal to

a=(2==2)
print(a)
a=(2==1)
print(a)
a=("hello"=="bye")
print(a)
a=("hello"=="hello")
print(a)
a=("Hello"=="hello")
print(a)
a=(3!=3)
print(a)
a=(1<3)
print(a)
a=(1>3)
print(a)
a=("1"==1)
print(a)
a=(2.0==2)
print(a)


## and, or, not

a=(1==1) or  (3<1)	# this result is true since requires only one condition to be true
print(a)
a=(1==1) and (3<1)	# this result is false since it requires both condition to be true
print(a)



