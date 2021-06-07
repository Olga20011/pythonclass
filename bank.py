from datetime import datetime
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
        if amount < 0:
            return"The amount should be more than 0"
        
        elif self.loan > 0:
            return f"Please repay your outstanding loan"
            
        elif amount >= 0.1*self.balance :
            return f"Your not qualified" 
        else:
            loan = amount *1.05
            self.loan=loan
            self.balance=+amount
            now=datetime.now()
            borrow={
            "amount":amount,
            "time":now,
            "narration":"Your account has been topped up with"}
            self.statement.append(borrow)

        return  f"Your account has now been topped up with {amount}"

    def pay(self,amount):
        if amount <0:
            return f"The amount must be grater than 0"
        elif amount < self.loan:
            self.loan-=amount
            return f" You have paid part of your loan with {amount} and {self.loan} is left" 
        else:
            diff=amount-self.loan
            self.loan=0
            self.deposit(diff)
            now=datetime.now()
            pay={
                "amount":amount,
                "time":now,
                "narration":"You have paid"
                
            }    
            self.statement.append(pay)
        return  f"You have cleared your loan and your account balance is {diff}"   

    def Show_statement(self):
        for transaction in self.statement:
                amount=transaction["amount"]
                narration=transaction["narration"]
                time=transaction["time"]
                date=time.strftime("%d/%m/%y")
                print(f"{date}:{narration} {amount}")      
        return  


        