class Bank_account():
	 
	 def __init__(self,name,balance):
	 	self.name=name
	 	self.balance=balance

	 def deposit(self,depo):
	 	self.balance=self.balance+depo
	 	print(f"you have a new balance of {self.balance}")	
	 		 
	 def withdraw(self, withd):
	 	if (self.balance-withd)>0:
	 		self.balance= self.balance-withd
	 		print(f"you have a new balance of {self.balance}")
	 	else:
	 		print("Insufficient Funds")	
	 	
name=input("what is your name? ")
balance= int(input("initial balance? "))
s=Bank_account(name,balance)
condition=True

while condition:
	operation= input("press 'd' to deposit or 'w' to withdraw ")
	if operation=="d":
		depo= int(input("what is the ammount you want to deposit? "))
		s.deposit(depo)
		condition2=input("you want to make a new deposit or withdraw ? (y/n)")
		if condition2.lower()=="n":
			condition=False
			print("GOOD BYE "+s.name)
		elif condition2.lower()!="y":
			print("no valid option 'GOOD BYE' "+s.name)
			condition=False

	elif operation=="w":
		withd= int(input("what is the ammount you want to withdraw? "))		
		s.withdraw(withd)
		condition2=input("you want to make a new deposit or withdraw ? (y/n)")
		if condition2.lower()=="n":
			condition=False
			print("GOOD BYE "+s.name)
		elif condition2.lower()!="y":
			print("no valid option 'GOOD BYE' "+s.name)
			condition=False

	else:
		print("option invalid")
		break

	




