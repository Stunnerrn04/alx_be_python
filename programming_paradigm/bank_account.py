# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if sufficient funds are available."""
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                print(f"Withdrew: ${amount:.2f}")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Invalid withdrawal amount.")
            return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current balance: ${self.account_balance:.2f}")
