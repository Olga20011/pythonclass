from datetime import datetime, time
class Account:
    def __init__(self,name,phone_Number): 
        self.name=name
        self.phone_Number=phone_Number
        self.balance=0
        self.loan=0
        self.repay=0
        self.statement=[]

    def show_balance(self):
        return f"Hello {self.name} your balance is  kshs{self.balance}"

    def deposit(self,amount):
        if amount<0:
            return f"amount can not be less than 0" 
        else:    
            self.balance += amount
            now=datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "narration":"You deposited"
            }
                
            self.statement.append(transaction)
        return self.show_balance()

    def withdraw(self,amount):
        if amount > self.balance:
            return f"Your balance is {self.balance} you can not withdraw {amount}"
        else:
            self.balance-=amount
            now=datetime.now()
            withdrawals={
                "amount":amount,
                "time":now,
                "narration":"You have withdrawn"
            }
            self.statement.append(withdrawals)
        return self.show_balance()    

    def borrow(self,amount):
        return  f"Your account has been topped up with {amount}"

    def pay(self,amount):
        return  f"You have repaid {amount}"   

    def Show_statement(self):
        for transaction in self.statement:
                amount=transaction["amount"]
                narration=transaction["narration"]
                time=transaction["time"]
                date=time.strftime("%d/%m/%y")
                print(f"{date}:{narration} {amount}")      
        return   

        