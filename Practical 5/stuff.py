class BankAccount:

    def __init__(self, holder, account_number, opening_balance=0.0):

        if not holder.strip():
            raise ValueError("Account holder cannot be blank")

        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative")

        self.holder = holder
        self.account_number = account_number
        self._balance = float(opening_balance)


    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return (f"BankAccount({self.holder}, "
                f"balance= {self._balance:.2f})")

    def __repr__(self):
        return (f"BankAccount(holder={self.holder!r}, "
                f"account_number={self.account_number!r}, "
                f"opening_balance={self._balance!r})")

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented

        return self._balance + other._balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


    def transfer_to(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Target must be a BankAccount")

        if amount <= 0:
            raise ValueError("Transfer amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds for transfer")

        self._balance -= amount
        other_account._balance += amount


class Student:
    def __init__(self, name, roll_number, marks):
        if not name.strip():
            raise ValueError("Name cannot be blank")
        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100")
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def __str__(self):
        return f"{self.name} (Roll {self.roll_number}) scored {self.marks}"

    def __repr__(self):
        return (f"Student(name={self.name!r}, "
                f"roll_number={self.roll_number!r}, "
                f"marks={self.marks!r})")




print("Test 1: Create account with opening balance 1500")
account1 = BankAccount("Asha", "BA101", 1500)
print("Object is created; balance is", account1.get_balance())
print()

print("Test 2: Deposit 250")
account1.deposit(250)
print("Balance becomes", account1.get_balance())
print()

print("Test 3: Withdraw 100")
account1.withdraw(100)
print("Balance becomes", account1.get_balance())
print()

print("Test 4: Withdraw more than balance")
try:
    account1.withdraw(9999)
except ValueError as e:
    print("ValueError:", e)
print()

print("Test 5: Deposit 0 or a negative amount")
try:
    account1.deposit(0)
except ValueError as e:
    print("ValueError:", e)
try:
    account1.deposit(-50)
except ValueError as e:
    print("ValueError:", e)
print()

print("Test 6: print(account1) and repr(account1)")
print(account1)
print(repr(account1))
print()

print("Test 7: account1 + account2")
account2 = BankAccount("Kabir", "BA102", 500)
print(account1 + account2)
print()

print("Extension: Readable and developer-oriented forms differ")
print("str  :", str(account1))
print("repr :", repr(account1))
print("Differ?", str(account1) != repr(account1))
print()

print("Extension: Returns the sum of both balances")
print("account1 balance =", account1.get_balance())
print("account2 balance =", account2.get_balance())
print("Sum =", account1 + account2)