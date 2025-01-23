class Customer():
    def __init__(self, name,surname, tc_identification, phone):
        self.name=name
        self.surname=surname
        self.tc_identification=tc_identification
        self.phone=phone
    def display_information(self):
        print( f "Name: {self.name} Surname: {self.surname} TR ID: {self.tc_identification} Phone: {self.phone}")
class account(Customer):
    def __init__ (self, name, surname, tc_identification, phone, account_number,balance=0)
        super().__init__(name, surname, tc_identification, phone)
        self.account_number=account_number
        self.balance=balance
    def deposit(self, amount):
        self.amount+=amount
        print (f"{amount} is deposited to the account. New balance is {self.balance}")
    def money_check(self, amount):
        if amount > self.balance:
            print("Insufficient balance. Withdrawal amount must equal to balance or less.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        else:
            self.balance -= amount
            print(f" {amount} Withdrew. New balance: {self.balance}")
    def display_balance(self):
        print(f"Account Balance: {self.balance}")
account = Account("Yasin", "Sinan", "12345678901", "+312583693", "123456789", 1500)
print(account)


        
    
