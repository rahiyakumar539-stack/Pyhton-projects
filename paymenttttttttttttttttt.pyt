import datetime

class PaymentApp:
    def __init__(self, username):
        self.username = username
        self.balance = 0
        self.history = []

    def add_balance(self, amount):
        self.balance += amount
        self.history.append(f"{datetime.datetime.now()} - Added ₹{amount}")
        print(f"₹{amount} added successfully!")

    def send_money(self, receiver, amount):
        if amount > self.balance:
            print("❌ Not enough balance!")
            return

        self.balance -= amount
        self.history.append(f"{datetime.datetime.now()} - Sent ₹{amount} to {receiver}")
        print(f"₹{amount} sent to {receiver} successfully!")

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")

    def show_history(self):
        if not self.history:
            print("No transactions yet.")
        else:
            print("\n📜 Transaction History:")
            for h in self.history:
                print("•", h)
                
app = PaymentApp(username="Rohit")

while True:
    print("\n===== Simple Payment App =====")
    print("1. Add Balance")
    print("2. Send Money")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = int(input("Enter amount to add: ₹"))
        app.add_balance(amt)

    elif choice == "2":
        receiver = input("Enter receiver name: ")
        amt = int(input("Enter amount to send: ₹"))
        app.send_money(receiver, amt)

    elif choice == "3":
        app.check_balance()

    elif choice == "4":
        app.show_history()

    elif choice == "5":
        print("Thank you for using the app!")
        break

    else:
        print("Invalid choice, try again!")
       

