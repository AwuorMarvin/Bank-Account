class BankAccount(object):
    def __init__(self, account_balance = 500):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.amount = amount
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            return 'Your account balance is insufficient'

class LeastBalance(BankAccount):
    def __init__(self, least_amount = 200):
        self.least_amount = least_amount