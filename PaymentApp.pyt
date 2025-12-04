import datetime

class PaymentApp:

    def __init__(self):
        self.balance = 0
        self.transactions = []   # Stores ("Paid"/"Added", amount, date)
        self.pin = "1234"        # Default PIN
        self.daily_limit = 200   # Daily Spending Limit ($200)

    # ------------------------------
    #   PIN LOGIN SYSTEM
    # ------------------------------
    def login(self):
        print("\n\U0001F510 Welcome to SecurePay")
        for attempt in range(3):
            user_pin = input("Enter your 4-digit PIN: ")
            if user_pin == self.pin:
                print("\u2705 Login Successful!\n")
                return True
            else:
                print("\u274C Wrong PIN!")

        print("\u26A0 Too many attempts! Locked Out.")
        return False

    # ------------------------------
    #   ADD MONEY
    # ------------------------------
    def add_money(self):
        amount = float(input("\U0001F4B0 Enter amount to add: "))
        self.balance += amount

        self.transactions.append(("Added", amount, datetime.date.today()))
        print(f"\u2705 Added ${amount}. New Balance: ${self.balance}")

    # ------------------------------
    #   CALCULATE TODAY SPENDING
    # ------------------------------
    def today_spent(self):
        today = datetime.date.today()
        spent = sum(t[1] for t in self.transactions if t[0] == "Paid" and t[2] == today)
        return spent

    # ------------------------------
    #   PAY MONEY
    # ------------------------------
    def pay_money(self):
        amount = float(input("\U0001F5FE Enter amount to pay: "))

        if amount > self.balance:
            print("\u274C Not enough balance!")
            return

        spent_today = self.today_spent()
        if spent_today + amount > self.daily_limit:
            print(f"\u26A0 You crossed daily limit of ${self.daily_limit}!")
            print(f"Today You Spent: ${spent_today}")
            return

        self.balance -= amount
        self.transactions.append(("Paid", amount, datetime.date.today()))
        print(f"\u2705 Payment Successful! Paid: ${amount}")
        print(f"Remaining Balance: ${self.balance}")

    # ------------------------------
    #   SHOW TRANSACTION HISTORY
    # ------------------------------
    def show_history(self):
        if not self.transactions:
            print("\U0001F4C1 No transactions yet.")
            return

        print("\n\U0001F4DC TRANSACTION HISTORY")
        for t in self.transactions:
            print(f"{t[0]}  |  ${t[1]}  |  {t[2]}")

    # ------------------------------
    #   MAIN MENU
    # ------------------------------
    def menu(self):
        if not self.login():
            return

        while True:
            print("\n--------- MENU ---------")
            print("1. Add Money")
            print("2. Pay Money")
            print("3. Transaction History")
            print("4. Check Today Spending")
            print("5. Check Balance")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_money()
            elif choice == "2":
                self.pay_money()
            elif choice == "3":
                self.show_history()
            elif choice == "4":
                print(f"Today You Spent: ${self.today_spent()}")
            elif choice == "5":
                print(f"\U0001F4B5 Current Balance: ${self.balance}")
            elif choice == "6":
                print("\U0001F44B Thank you for using SecurePay")
                break
            else:
                print("\u274C Invalid option!")

# Run the App
app = PaymentApp()
app.menu()
