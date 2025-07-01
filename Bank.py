customers = []

class Account:
    def __init__(self, owner, pin, balance=0):
        self.owner = owner
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("✅ Deposited", amount)
        else:
            print("❌ Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("✅ Withdrew", amount)
            else:
                print("⚠️ Insufficient balance")
        else:
            print("❌ Invalid withdrawal amount")

    def display_balance(self):
        print("👤 Account Owner:", self.owner)
        print("💰 Current Balance:", self.balance)


class SavingsAccount(Account):
    def __init__(self, owner, pin, balance=0):
        super().__init__(owner, pin, balance)
        self.interest_rate = 0.03

    def add_interest(self):
        time = float(input("⏳ Enter time in years: "))
        rate = self.interest_rate * 100
        amount = self.balance * ((1 + rate / 100) ** time)
        interest = amount - self.balance
        self.balance = amount
        print("📈 Compound Interest added:", interest)


class CurrentAccount(Account):
    def __init__(self, owner, pin, balance=0):
        super().__init__(owner, pin, balance)
        self.overdraft_limit = 500

    def withdraw(self, amount):
        if amount > 0:
            if self.balance + self.overdraft_limit >= amount:
                self.balance -= amount
                print("✅ Withdrew", amount)
            else:
                print("🚫 Overdraft limit exceeded")
        else:
            print("❌ Invalid withdrawal amount")


def welcome_screen():
    print("\n" + "=" * 40)
    print("🏦  WELCOME TO PYTHON BANK SYSTEM  🏦")
    print("=" * 40 + "\n")


def create_account():
    name = input("👤 Enter your name: ")
    pin = input("🔐 Set a 4-digit PIN: ")

    print("\n🧾 Choose Account Type:")
    print("1️⃣  Savings Account")
    print("2️⃣  Current Account")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        acc = SavingsAccount(name, pin)
    elif choice == "2":
        acc = CurrentAccount(name, pin)
    else:
        print("❌ Invalid choice")
        return

    customers.append((acc, pin))
    print("✅ Account created successfully!")


def login():
    name = input("👤 Enter your name: ")
    pin = input("🔑 Enter your PIN: ")

    for account, account_pin in customers:
        if account.owner == name and account.pin == pin:
            print("🔓 Login successful!")
            return account

    print("❌ Login failed! Invalid name or PIN.")
    return None


def user_menu(account):
    while True:
        print("\n🔧 Choose Operation:")
        print("1️⃣  Deposit 💵")
        print("2️⃣  Withdraw 🏧")
        print("3️⃣  Check Balance 📊")
        if isinstance(account, SavingsAccount):
            print("4️⃣  Add Interest 📈")
        print("0️⃣  Logout 🚪")

        option = input("➡️  Enter your choice: ")

        if option == "1":
            amt = int(input("💵 Enter amount to deposit: "))
            account.deposit(amt)
        elif option == "2":
            amt = int(input("🏧 Enter amount to withdraw: "))
            account.withdraw(amt)
        elif option == "3":
            account.display_balance()
        elif option == "4" and isinstance(account, SavingsAccount):
            account.add_interest()
        elif option == "0":
            print("👋 Logged out successfully.")
            break
        else:
            print("❌ Invalid option. Please try again.")


def show_all_customers():
    print("\n👥 List of All Customers:")
    if not customers:
        print("No customers found.")
    else:
        for i, (cust, _) in enumerate(customers):
            acct_type = "Savings" if isinstance(cust, SavingsAccount) else "Current"
            print(str(i + 1) + ".", "Name:", cust.owner, "| Type:", acct_type, "| Balance:", cust.balance)


def main():
    welcome_screen()

    while True:
        print("\n🏦 Main Menu:")
        print("1️⃣  Create New Account")
        print("2️⃣  Login to Account")
        print("3️⃣  View All Customers")
        print("0️⃣  Exit")

        choice = input("➡️  Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            user = login()
            if user:
                user_menu(user)
        elif choice == "3":
            show_all_customers()
        elif choice == "0":
            print("🙏 Thank you for using Python Bank System. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice.")



main()
