"""
Implement a class called `BankAccount` that models a simple bank account.

The class should have the following methods:

- `__init__(owner, balance=0)`
    Initialize a new bank account with the account owner's name and an
    optional starting balance. If no balance is provided, the balance
    should default to 0.

- `deposit(amount)`
    Increase the account balance by `amount`.

- `withdraw(amount)`
    Decrease the account balance by `amount` if sufficient funds are
    available. If the withdrawal would result in a negative balance,
    raise a `ValueError` with an appropriate error message.

- `display()`
    Return a string in the following format:

        "<owner>'s balance: $<balance>"

You may assume that deposit amounts are always positive integers.

Do not write any code outside of the class definition.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def display(self):
        return f"{self.owner}'s balance: ${self.balance}"


def main():
    account = BankAccount("Alice", 100)

    account.deposit(50)
    print(account.display())

    account.withdraw(30)
    print(account.display())

    try:
        account.withdraw(200)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()