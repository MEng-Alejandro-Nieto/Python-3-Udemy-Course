from first_folder import first_level
from first_folder.second_folder import second_level

first_level.func1()
second_level.func2()

if __name__=='__main__':
	print("is directly")
else:
	print("is imported")


