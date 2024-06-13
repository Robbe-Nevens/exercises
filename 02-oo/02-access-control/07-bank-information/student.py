class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("​Cannot deposit zero or negative funds")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("​Cannot deposit zero or negative funds")
        if self.__balance - amount < 0:
            raise ValueError("insufficient funds")
        self.__balance -= amount

