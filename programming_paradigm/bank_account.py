# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount instance with a given initial balance.
        :param initial_balance: Initial balance of the account (default is 0)
        """
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        :param amount: The amount to deposit
        """
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if sufficient funds are available.
        :param amount: The amount to withdraw
        :return: True if withdrawal is successful, False otherwise
        """
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew ${amount:.2f}.")
            return True
        elif amount > self._account_balance:
            print("Insufficient funds.")
            return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Display the current balance of the account.
        """
        print(f"Current balance: ${self._account_balance:.2f}")
