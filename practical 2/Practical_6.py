class BankAccount:
    def __init__(self, holder, account_number, opening_balance=0.0):
        if not holder.strip():
            raise ValueError("Account holder cannot be blank")
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative")
        self.holder = holder
        self.account_number = account_number
        self._balance = float(opening_balance)

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

    # Extension 1: safe transfer between two accounts
    def transfer_to(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Target must be a BankAccount")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds for transfer")
        self._balance -= amount
        other_account._balance += amount

    # Extension 2: read only balance property
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
        # Returns combined balance without modifying either account
        return self._balance + other._balance


# Extension 3: Student class with __str__ and __repr__
class Student:
    def __init__(self, name, roll_number, marks):
        if not name.strip():
            raise ValueError("Student name cannot be blank")
        if roll_number <= 0:
            raise ValueError("Roll number must be positive")
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def __str__(self):
        return f"Student({self.name}, roll= {self.roll_number}, marks= {self.marks})"

    def __repr__(self):
        return (f"Student(name={self.name!r}, "
                f"roll_number={self.roll_number!r}, "
                f"marks={self.marks!r})")


def run_tests():
    print("=== BankAccount basics ===")
    account1 = BankAccount("Asha", "BA101", 1500)
    account2 = BankAccount("Kabir", "BA102", 500)

    account1.deposit(250)
    account2.withdraw(100)

    print(account1)
    print(repr(account1))
    print("Balance:", account1.get_balance())
    print("Combined:", account1 + account2)

    print("\n=== Invalid operations ===")
    try:
        account1.withdraw(999999)
    except ValueError as e:
        print("Withdraw error:", e)
    try:
        account1.deposit(0)
    except ValueError as e:
        print("Deposit error:", e)

    print("\n=== Transfer extension ===")
    account1.transfer_to(account2, 300)
    print("account1 balance:", account1.get_balance())
    print("account2 balance:", account2.get_balance())

    print("\n=== Balance property ===")
    print("Read via property:", account1.balance)
    try:
        account1.balance = 9999
    except AttributeError as e:
        print("Assignment blocked:", e)

    print("\n=== Student class ===")
    student = Student("Riya", 12, 87)
    print(student)
    print(repr(student))


if __name__ == "__main__":
    run_tests()
