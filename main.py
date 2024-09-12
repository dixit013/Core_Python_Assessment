# main.py
from banker import Banker

def main():
    banker = Banker()
    
    while True:
        print("\nBank Management System")
        print("1. Add Customer")
        print("2. View Customer")
        print("3. Search Customer")
        print("4. View All Customers")
        print("5. Total Amount in Bank")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter customer name: ")
            account_number = input("Enter account number: ")
            balance = float(input("Enter balance: "))
            banker.add_customer(name, account_number, balance)
        
        elif choice == '2':
            account_number = input("Enter account number: ")
            banker.view_customer(account_number)
        
        elif choice == '3':
            name = input("Enter customer name to search: ")
            banker.search_customer(name)
        
        elif choice == '4':
            banker.view_all_customers()
        
        elif choice == '5':
            banker.total_amount_in_bank()
        
        elif choice == '6':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
