#ANSWER5: 

class Customer:
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print(f"Customer Information:\nName: {self.name} {self.surname}\nTC ID: {self.tc_identification}\nPhone: {self.phone}")


class Account(Customer):
    def __init__(self, customer, account_number, balance=0):
        super().__init__(customer.name, customer.surname, customer.tc_identification, customer.phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount} TL. New balance: {self.balance} TL.")
        else:
            print("Invalid deposit amount.")

    def money_check(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn: {amount} TL. New balance: {self.balance} TL.")
            else:
                print("Insufficient balance for this transaction.")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account Balance: {self.balance} TL")


# Example Usage
# Create a Customer object
customer1 = Customer(name="Ahmet", surname="Yilmaz", tc_identification="12345678901", phone="05551112233")

# Create an Account object associated with the customer
account1 = Account(customer=customer1, account_number="TR1234567890123456", balance=1000)

# Display customer information
customer1.display_information()

# Perform account operations
account1.display_balance()
account1.deposit(500)  # Deposit money
account1.money_check(300)  # Withdraw money
account1.money_check(1500)  # Attempt to withdraw more than the balance
account1.display_balance()
