#mvp advanced ATM Iterface lab 
import atm_interface

acc1 = atm_interface.CheckingAccount(100)
acc2 = atm_interface.SavingsAccount(100)

while True:
    try:
        choice = input("""Please select from the following menu:
            1. Checking account balance
            2. Withdraw from checking
            3. Deposit into Checking
            4. Savings account balance
            5. Withdraw from Savings
            6. Deposit into Savings """)
    except ValueError:
        continue
    if choice == "1":
        acc1.get_funds()
    elif choice == "2":
        cash = int(input("Enter amount to withdraw: "))
        acc1.withdraw(cash)
    elif choice == "3":
        amount = int(input("Enter amount to deposit: "))
        acc1.deposit(amount)
    elif choice == "4":
        acc2.get_funds()
    elif choice == "5":
        amount = int(input("Enter amount to withdraw: "))
        acc2.withdraw(amount)
    elif choice == "6":
        amount = int(input("Enter amount to deposit: "))
        acc2.deposit(amount)
