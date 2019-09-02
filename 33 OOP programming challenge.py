'''
 Create a bank account  class that has two attributes:
1. Owner
2. Balance

And two methods:
1. Deposit
2. Withdraw (which can't exceed the available balance)
'''

class Account():
	owner="Jose"
	balance=100

	def deposit(self,depo):
		new_balance = self.balance+depo
		return f"you just add {depo} and your new balance is {new_balance}"

	def withdraw(self,withd):

		if withd<self.balance:
			new_balance = self.balance-withd
			return f"you just withdraw {withd} and your new balance is {new_balance}"
		else:
			return f"you can't withdraw {withd} since your balance is {self.balance}"


action=Account()
deposit=action.deposit(50)
withdraw=action.withdraw(90)
withdraw2=action.withdraw(101)
print(action.owner)
print(action.balance)
print(deposit)
print(withdraw)
print(withdraw2)








