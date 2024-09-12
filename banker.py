# banker.py
from customerr import Customer

class Banker:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, account_number, balance):
        if account_number in self.customers:
            print("Customer with this account number already exists.")
        else:
            self.customers[account_number] = Customer(name, account_number, balance)
            print("Customer added successfully.")

    def view_customer(self, account_number):
        customer = self.customers.get(account_number)
        if customer:
            print(customer)
        else:
            print("Customer not found.")

    def search_customer(self, name):
        found = False
        for customer in self.customers.values():
            if customer.name.lower() == name.lower():
                print(customer)
                found = True
        if not found:
            print("No customer found with that name.")

    def view_all_customers(self):
        if self.customers:
            for customer in self.customers.values():
                print(customer)
        else:
            print("No customers in the bank.")

    def total_amount_in_bank(self):
        total = sum(customer.balance for customer in self.customers.values())
        print(f"Total amount in the bank: ${total:.2f}")
