class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\n Account '{self.name}' created.\n Balance = ${self.balance:.2f}") 


    def getBalance(self):
        print(f"\n Account '{self.name}' balance = ${self.balance:.2f} ")

    def deposit(self, amount):
        self.balance += amount
        print(f"\n Deposit complete.") 
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' balance is only ${self.balance:.2f}"
            )
        

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\n Withdrawal complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw interrupted: {error}')    
            
    def transfer(self, amount, account):
        try:
            print('\n ************\n\n Beginning Transfer... ')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\n ************\n\n Transfer complete.')
        except BalanceException as error:
            print(f'\n Transfer interrupted: {error}')
            
class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print(f"\n Deposit complete.")
        self.getBalance()
        
class SavingsAcct(InterestRewardAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n Withdrawal complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw interrupted: {error}')