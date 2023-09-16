class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited {amount} INR into the account.")

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew {amount} INR from the account.")
        else:
            print("Withdrawal failed. Insufficient funds.")

    def display_balance(self):
        print(f"Account balance for {self._account_holder_name} (Account #: {self._account_number}): {self._account_balance} INR")


# Example usage
if __name__ == "__main__":
    # Create an instance of the BankAccount class
    my_account = BankAccount("1234567890", "Your Name", 10000)  # Replace with your account details

    # Test deposit and withdrawal functionality
    my_account.display_balance()
    my_account.deposit(5000)
    my_account.display_balance()
    my_account.withdraw(2000)
    my_account.display_balance()
    my_account.withdraw(10000)  # Attempt to withdraw more than the balance