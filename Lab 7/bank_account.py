class BankAccount :
    
    def __init__(self, bank_name, owner_name, account_number, balance) :
        self.__bank_name = bank_name
        self.__owner_name = owner_name
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, money) :
        self.__balance += money
        
    def withdraw(self, money) :
        self.__balance -= money
    
    def print_out(self) :
        print("Bank Name:", self.__bank_name)
        print("Owner Name:", self.__owner_name)
        print("Account Number:", self.__account_number)
        print("Your current balance:", self.__balance)
        
my_account = BankAccount("Krung Ter", "Pottarr", 69420, 0)

my_account.print_out()
my_account.deposit(12345)
my_account.print_out()
my_account.withdraw(6969)
my_account.print_out()