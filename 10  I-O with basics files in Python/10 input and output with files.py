# mode = 'r'	Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
# mode = 'w'	Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# mode = 'a'	Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# mode = 'r+'	Opens a file for both reading and writing. The file pointer placed at the beginning of the file (Does not overwrite)
# mode = 'w+'	Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

# When trying this code open the file "myfyle.txt" and write the first three lines


with open("myfile.txt", mode="r") as f:		# creates  indentation and set the variable f as the file in reading mode
	a=f.read()								# reads the file f and assign it to the variable "a"
	print(a)								# prints the value assigned to "a"
	
with open("myfile.txt",mode="a") as f:		# creates  indentation and set the variable f as the file in appending mode
	f.write("fourth line\nfifth line\n")		# write in a new line of "myfile.txt" the phrase "fourth line" and the a new line and "fifth line"

with open("newfile.txt", mode="w") as f:								# creates or overwrites "newfile.txt" 
	f.write("this is file was created with python")	# writes what is in the quotes	
	#print(f.read())	##### this line will not print anything and will throw and error since mode="w" only writes and can no read

with open("newfile2.txt", mode="w+") as f:								# creates or overwrites "newfile.txt" 
	f.write("this is the first line of the file created with python")	# writes what is in the quotes	
	f.seek(0)															# set the cursor back to position 0	to read
	print(f.read())														# prints everything  and the cursor will be in the last position





