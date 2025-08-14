
class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f} to {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.account_holder}'s account.")
        else:
            print("Insufficient funds or invalid amount.")


    def display_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.__balance:.2f}")


    def _get_balance(self):
        return self.__balance


    def _set_balance(self, amount):
        self.__balance = amount


    def __str__(self):
        return f"Account({self.account_number}, Holder: {self.account_holder}, Balance: ${self.__balance:.2f})"


    def __eq__(self, other):
        if isinstance(other, Account):
            return self.account_number == other.account_number
        return False



class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif self._get_balance() - amount < 100:
            print("Cannot withdraw: Minimum balance of $100 must be maintained.")
        else:
            self._set_balance(self._get_balance() - amount)
            print(f"Withdrew ${amount:.2f} from savings account.")



class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif self._get_balance() - amount < -self.overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            self._set_balance(self._get_balance() - amount)
            print(f"Withdrew ${amount:.2f} from checking account.")



if __name__ == "__main__":

    savings = SavingsAccount("SA001", "Alice", 500, interest_rate=0.03)
    checking = CheckingAccount("CA001", "Bob", 200, overdraft_limit=300)


    savings.deposit(100)
    savings.withdraw(450)  
    savings.withdraw(200)  


    checking.deposit(50)
    checking.withdraw(600)  
    checking.withdraw(400)

    savings.display_balance()
    checking.display_balance()

    print(savings)
    print(checking)
    print("Accounts equal?", savings == checking)
    print("Accounts equal?", savings == SavingsAccount("SA001", "Alice", 300))
