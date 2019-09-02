mylist=[1,2,3]
print(len(mylist))

class Book():
	def __init__(self,title,author,pages):
		self.title=title
		self.author=author
		self.pages=pages
b=Book("python rocks","jose","200")
print(b)	#this will print the location at the memory
# in order to print information from inside a class, we do

class Book2():
	def __init__(self,title,author,pages):
		self.title=title
		self.author=author
		self.pages=pages
	def __str__(self):
		return f"{self.title} was written by {self.author} and has {self.pages} pages"
	def __len__(self):
		return len(self.pages)
	def __del__(self):
		print("something has been deleted")
c=Book2("Termodinamica","Cenguel","6111")
print(str(c))
print(len(c))
del c



