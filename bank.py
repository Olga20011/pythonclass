class Bank:
    def __init__(self ,accountName,accountNumber):
        self.accountName=accountName
        self.accountNumber=accountNumber
    def balance(self):
        return (f"Dear {self.accountName} your balance is 400kshs")
    def withdraw(self):
        return (f"Dear {self.accountName},{self.accountNumber} you have withdrawn 500kshs"  )     