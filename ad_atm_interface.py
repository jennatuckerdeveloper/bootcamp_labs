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

    def get_standing(self):

        """
        This function returns a bool telling whether the account has
        more than $1,000 in it.

        test1 = Account(1001)
        test2 = Account(999)

        >>> get_standing(test1)
        True

        >>> get_standing(test2)
        False

        """

        if self._balance >= 1000:
            return True
        elif self._balance < 1000:
            return False

    def bank_greed(self):
        profits = 0
        if self._balance <= 0:
            self._balance -= 25
            profits += 25
        return self._balance
        #the withdraw method would call this method if self._balance <= 0

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
# acc1 = Account(999)
# print(acc1.get_standing())
# acc2 = Account()
# # print(acc2.get_standing())
# print(acc2.bank_greed())

"""
Save the account balance to a file after each operation.
Read that balance on startup so the balance persists across program starts.

Add to each account class an account ID number.

Allow the user to open more than one account.
Let them perform all of the above operations by account number.

"""
