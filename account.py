class BankAccount:
    account_counter = 1000 # Class variable or Global variable 
    def __init__(self,name,balance=0):
        self.name = name 
        self.__balance = balance # Private Access Modifier 
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1 # Icreament Class variable By One 
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount 
            print(f"Deposited {amount}.New Balance Is {self.__balance}")
        else:
            print("Deposited Amount Must be Greater Than 0.")
    
    def withdraw(self,amount):
        if amount > 0 <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount}. New Balance Is {self.__balance}")
        else:
            print("Withdrawl amount Must Be Grater Than 0 And Less Than Available balance  ")
    
    def display_account_info(self):
        print(f"Account Number :{self.account_number},Balance {self.__balance}")

class Savings_Account(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.02):
        super().__init__(name, balance)
        self.intrest_rate = interest_rate
    
    def calculate_interest(self):
        interest = self.get_balance() * self.intrest_rate
        self.diposit(interest)
        print(f"Applied Interest Od {interest}. New Balance Is {self.get_balance()}. ")
    
class Current_Account(BankAccount):
    def _init_(self, name, balance=0, overdraft_limit=5000):
        super()._init_(name, balance)
        self.overdraft_limit = overdraft_limit