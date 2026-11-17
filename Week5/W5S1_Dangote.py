# ==========================================================
# dangote_bank.py  –  complete solution
# ==========================================================

class BankAccount:
    """Represents one client's bank account."""

    def __init__(self, owner, account_number, balance=0):
        # owner          – name of the client
        # account_number – unique number for this account
        # balance        – starting money (default 0)
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Remove money from the account if there is enough."""
        if amount <= 0:
            print("Withdraw amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def view_balance(self):
        """Show the current balance."""
        print(f"Account {self.account_number} ({self.owner}): {self.balance}")
        return self.balance


class Bank:
    """Manages many BankAccount objects and allows transfers."""

    def __init__(self, name):
        self.name = name
        # Dictionary of accounts: key = account_number, value = BankAccount object
        self.accounts = {}

    def create_account(self, owner, account_number, balance=0):
        """Open a new account for a client."""
        if account_number in self.accounts:
            print("Account number already exists.")
            return
        account = BankAccount(owner, account_number, balance)
        self.accounts[account_number] = account
        print(f"Account {account_number} created for {owner}.")

    def get_account(self, account_number):
        """Return the BankAccount object or None if not found."""
        return self.accounts.get(account_number)

    def transfer(self, from_acc, to_acc, amount):
        """Transfer money from one account to another."""
        source = self.get_account(from_acc)
        target = self.get_account(to_acc)

        if source is None or target is None:
            print("One or both accounts not found.")
            return
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        if source.balance < amount:
            print("Insufficient funds for transfer.")
            return

        source.balance -= amount
        target.balance += amount
        print(f"Transferred {amount} from {from_acc} to {to_acc}.")
        print(f"  {source.owner} new balance: {source.balance}")
        print(f"  {target.owner} new balance: {target.balance}")


# ===== Example usage =====
if __name__ == "__main__":
    bank = Bank("Dangote Bank")

    bank.create_account("Alice", "ACC001", 1000)
    bank.create_account("Bob", "ACC002", 500)

    alice = bank.get_account("ACC001")
    bob = bank.get_account("ACC002")

    alice.deposit(200)
    alice.withdraw(100)
    alice.view_balance()

    bank.transfer("ACC001", "ACC002", 300)
    bob.view_balance()
