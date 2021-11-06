# This class simulates a bank account

class BankAccount:

    # the __init__ method accepts an argument for the account balance.
    # it is assigned to the __balance attribute


    def __init__ (self,bal):
        self.__balance = bal

    # This deposit method makes a deposit into the account

    def deposit(self, amount):
        self.__balance += amount

    # This withdraw method withdraw an amount from the account
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount

        else:
            print("Error: Insufficient Balance")


    # The get_balance mathod ruturns the account balance
    def get_balance(self):
        return self.__balance