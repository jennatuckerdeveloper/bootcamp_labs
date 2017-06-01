#mvp for Advanced ATM Inferface lab 

class Account:
    def __init__(self, balance=0, interest_rate=.01):
        #Those are defaults, so if you enter nothing, it will set to those.
        self._balance = balance
        self._interest_rate = interest_rate
        #print(self._balance)
        #print(self._interest_rate)
    def get_funds(self):
        #return self._balance
        print(self._balance)
    def deposit(self, amount):
        self._balance += amount
        print(self._balance)
    def check_withdrawal(self, amount):
        if self._balance > amount:
            return True
        else:
            return False
    def withdraw(self, amount):
        status = self.check_withdrawal(amount)
        if status == True:
            self._balance -= amount
            print(self._balance)
    def calc_interest(self):
        self._balance = self._interest_rate * self._balance + self._balance
        print(self._balance)

class SavingsAccount(Account):

    def __init__(self, balance=0, interest_rate=.01):
        super().__init__(balance, interest_rate)

class CheckingAccount(Account):

    def __init__(self, balance=0, interest_rate=.01):
        super().__init__(balance, interest_rate)

# acc1 = Account(100)
# acc1.get_funds()
# acc1.deposit(100)
# acc1.check_withdrawal(201)
# acc1.withdraw(100)
# acc1.withdraw(101)
# acc1.calc_interest()
