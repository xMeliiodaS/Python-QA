class BankAccount:

    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance


    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        if isinstance(value, str):
            self._account_number = value
        else:
            print("Please enter a string")

    def deposit(self, value):
        if value >= 0:
            self._balance += value
        else:
            print("Can't enter negative number")

    def withdraw(self, value):
        if value >= 0:
            self._balance -= value
        else:
            print("Can't enter negative number")

    def get_balance(self):
        return self._balance
