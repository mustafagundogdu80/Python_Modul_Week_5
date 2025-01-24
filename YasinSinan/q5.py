class Customer():
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"TC Identification: {self.tc_identification}")
        print(f"Phone: {self.phone}")


class Account(Customer):
    def __init__(self, name, surname, tc_identification, phone, account_number, balance=0):
        super().__init__(name, surname, tc_identification, phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} is deposited to the account. New balance is {self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance. Withdrawal amount must equal to balance or less.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def display_balance(self):
        print(f"Account Balance: {self.balance}")


# Test
customer1 = Customer("Yasin", "Sinan", "12345678901", "+312583693")
account1 = Account("Yasin", "Sinan", "12345678901", "+312583693", "123456789", 1500)

customer1.display_information()  # Müşteri bilgilerini gösterir
account1.display_balance()       # Mevcut hesabın bakiyesini gösterir

account1.deposit(200)            # 200 birim para yatırılır
account1.withdraw(100)           # 100 birim para çekilir
account1.withdraw(1700)          # Yetersiz bakiye
account1.display_balance()       # Son bakiyeyi gösterir
