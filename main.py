from Banking.account import Savings_Account, Current_Account
from Banking.transactions import withdraw, deposit
accounts = {}

def create_account():
    name = input("Enter your name: ").strip()
    acc_type = input("Enter Account Type (Savings/Current): ").strip().lower()
    initial_deposit = float(input("Enter Initial balance: "))
    
    if acc_type == "savings":
        acc = Savings_Account(name, initial_deposit)
    elif acc_type == "current":
        acc = Current_Account(name, initial_deposit)
    else:
        print("Invalid account type!")
        return
    accounts[acc.account_number] = acc 
    print(f" Account Created Successfully. Account Number Is : {acc.account_number}")







