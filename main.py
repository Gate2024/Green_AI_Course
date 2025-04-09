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

def login():
    acc_no = eval(input("Enter your account number: "))
    if acc_no in accounts:
        user_acc = accounts[acc_no]
        print(f"Welcome, {user_acc.name}")
        
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            if isinstance(user_acc, Savings_Account):
                print("4. Calculate Interest")
            print("5. Logout")
            action = input("Choose an option: ").strip()
            if action == "1":
                amount = float(input("Enter amount to deposit: "))
                deposit(user_acc, amount)
            elif action == "2":
                amount = float(input("Enter amount to withdraw: "))
                withdraw(user_acc, amount)
            elif action == "3":
                print(f"Your balance: {user_acc.get_balance()}")
            elif action == "4" and isinstance(user_acc, Savings_Account):
                user_acc.calculate_interest()
            elif action == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice!")
    else:
        print("Account not found!")

        
def main():
    print("\n======== WELCOME to SBI Bank ==========")
    print("======== Chhatrapati MAIN CITY BRANCH =============")
    
    while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank you for using our service!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()







