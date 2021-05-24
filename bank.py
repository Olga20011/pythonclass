class Account:
    def __init__(self,name,phone_Number): 
        self.name=name
        self.phone_Number=phone_Number
        self.balance=0
        self.loan=0
        self.repay=0

    def show_balance(self):
        return f"Hello {self.name} your balance is  kshs{self.balance}"

    def deposit(self,amount):
        if amount<0:
            return f"amount can not be less than 0" 
        else:    
            self.balance += amount
        return self.show_balance()

    def withdraw(self,amount):
        if amount > self.balance:
            return f"Your balance is {self.balance} you can not withdraw {amount}"
        else:
            self.balance-=amount
            return self.show_balance()    

    def borrow(self,amount):
        return  f"Your account has been topped up with {amount}"

    def pay(self,amount):
        return  f"You have repaid {amount}"    

        