from bank_accounts import *

Moroni = BankAccount(1000, "Moroni")
Jarede = BankAccount(100, "Jarede")

Moroni.getBalance()
Jarede.getBalance()


Moroni.withdraw(20)

Moroni.transfer(10, Jarede)

Cora = InterestRewardAcct(100, "Cora")
Cora.getBalance()

Cora.deposit(100)

Rebeca = InterestRewardAcct(100, "Rebeca")

Cora.transfer(20, Rebeca)

Dudu = SavingsAcct(100, "Dudu")

Dudu.getBalance()

Dudu.deposit(100)

Dudu.transfer(10, Moroni)