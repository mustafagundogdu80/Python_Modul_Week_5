# Question5: Create a "Customer" class and an "Account" class. Let the "Account" class inherit from the "Customer" class and represent a customer's bank account information.

# Customer Class Features:
#     "name" (customer name)
#     "surname" (customer surname)
#     "tc_identification" (customer TR ID number)
#     "phone" (customer phone number)
# Account Class Properties:
#     "customer" (a Customer object)
#     "account_number" (account number)
#     "balance" (account balance)
# Customer Class Method:
#     "display_information()": Displays the customer's name, surname, TR ID number and telephone number.
# Account Class Methods:
#     "deposit(self, amount)": A method that deposits a certain amount of money into the account.
#     "money_check(self, amount)": A method that withdraws a certain amount of money from the account. However, if there is not enough balance in the account, the transaction should not occur and a message should be displayed.
#     "display_balance()": A method that displays the account balance.
# Create these two classes, then create a Customer object and an Account object, add the customer information to the Account object, and perform account operations and view the results.


# Soru5: Bir “Müşteri” sınıfı ve bir “Hesap” sınıfı oluşturun. “Account” sınıfı ‘Customer’ sınıfından miras alsın ve bir müşterinin banka hesap bilgilerini temsil etsin.

# Müşteri Sınıfı Özellikleri:
#     “name” (müşteri adı)
#     “surname” (müşteri soyadı)
#     “tc_identification” (müşteri TC Kimlik numarası)
#     “phone” (müşteri telefon numarası)
# Hesap Sınıfı Özellikleri:
#     “customer” (bir Customer nesnesi)
#     “account_number” (hesap numarası)
#     “balance” (hesap bakiyesi)
# Müşteri Sınıfı Yöntemi:
#     “display_information()": Müşterinin adını, soyadını, TC kimlik numarasını ve telefon numarasını görüntüler.
# Hesap Sınıfı Metotları:
#     “deposit(self, amount)": Hesaba belirli bir miktar para yatıran bir metottur.
#     “para_çek(self, tutar)": Hesaptan belirli bir miktarda para çeken bir yöntemdir. Ancak hesapta yeterli bakiye yoksa işlem gerçekleşmemeli ve bir mesaj görüntülenmelidir.
#     “display_balance()": Hesap bakiyesini görüntüleyen bir yöntem.
# Bu iki sınıfı oluşturun, ardından bir Customer nesnesi ve bir Account nesnesi oluşturun, müşteri bilgilerini Account nesnesine ekleyin ve hesap işlemlerini gerçekleştirip sonuçları görüntüleyin.


# Customer Sınıfı
class Customer:
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print(f"Customer Info - Name: {self.name}, Surname: {self.surname}, TC ID: {self.tc_identification}, Phone: {self.phone}")

# Account Sınıfı
class Account(Customer):
    def __init__(self, customer, account_number, balance=0):
        self.customer = customer
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def money_check(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")

    def display_balance(self):
        print(f"Account Balance: {self.balance}")

# Customer ve Account Nesneleri Oluşturma
customer = Customer("Ahmet", "Yılmaz", "12345678901", "05551234567")
account = Account(customer, "TR1234567890123456", 1000)

# Müşteri Bilgilerini Görüntüle
customer.display_information()

# Hesap İşlemleri
account.display_balance()
account.deposit(500)
account.money_check(2000)  # Yetersiz bakiye testi
account.money_check(800)   # Geçerli çekim testi
account.display_balance()
