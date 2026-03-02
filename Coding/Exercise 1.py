class BankAccount:
    def __init__(self, holder, initial_balance):
        self.holder = holder 
        self._bank = "Attijariwafa Bank" 
        self.__balance = initial_balance 
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of {amount} MAD completed")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of {amount} MAD completed")
        else:
            print(f"Insufficient funds! Available balance: {self.__balance} MAD")
    
    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return f"Account of {self.holder} | Balance: {self.__balance} MAD"

print("="*50)
print("EXERCISE 1 - Bank Account")
print("="*50)

account = BankAccount("Yasmine", 5000)
print(f"Account created: {account}")

account.deposit(2000)
account.withdraw(1000)

print(f"Balance via get_balance(): {account.get_balance()} MAD")
print(f"Display via print(): {account}")

print("\nAttempt to access account.__balance:")
try:
    print(account.__balance)
except AttributeError as e:
    print(f"Error: {e}")
    print("Explanation: __balance is a private attribute, it is 'name mangled' to _BankAccount__balance")
    print(f"Access possible via: {account._BankAccount__balance} (but this is not recommended)")
