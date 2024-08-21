# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Check if an initial balance is provided
    if len(sys.argv) > 1:
        try:
            initial_balance = float(sys.argv[1])
        except ValueError:
            print("Invalid initial balance. Please enter a numeric value.")
            return
    else:
        initial_balance = 0

    # Create a BankAccount instance
    account = BankAccount(initial_balance)

    # Display initial balance
    account.display_balance()

    # Provide options to the user
    while True:
        print("\nChoose an operation:")
        print("1: Deposit")
        print("2: Withdraw")
        print("3: Display Balance")
        print("4: Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        
        elif choice == '3':
            account.display_balance()

        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
