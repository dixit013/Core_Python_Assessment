# customer.py
class Customer:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Name: {self.name}, Account Number: {self.account_number}, Balance: ${self.balance:.2f}"
