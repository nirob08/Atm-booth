from abc import ABC, abstractmethod
import hashlib

# Base Account class with abstract methods
class Account(ABC):
    def __init__(self, name):
        self._name = name  # Encapsulation: name is private
        self._balance = 0  # Encapsulation: balance is private
        self._transactions = []  # Encapsulation: transactions are private

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative.")
        else:
            self._balance = amount

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def print_transactions(self):
        pass

# User class inherits from Account
class User(Account):
    def __init__(self, name, pin):
        super().__init__(name)
        self._pin = self.hash_pin(pin)  # Encapsulation: PIN is private

    def hash_pin(self, pin):
        return hashlib.sha256(pin.encode()).hexdigest()

    def verify_pin(self, pin):
        return self.hash_pin(pin) == self._pin

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(f"Deposited: ${amount}")
            print(f"Deposited ${amount}. New balance is: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Withdrew: ${amount}")
            print(f"Withdrew ${amount}. New balance is: ${self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def print_transactions(self):
        print(f"Transaction history for {self._name}:")
        for transaction in self._transactions:
            print(transaction)

# ATM class handles user interaction and polymorphism
class ATM:
    def __init__(self):
        self.users = {}
        self.login_attempts = {}

    def create_user(self, name, pin):
        if name in self.users:
            print("User already exists.")
        elif len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN. Please create a 4-digit PIN.")
        else:
            self.users[name] = User(name, pin)
            print(f"Account created successfully for {name}.")

    def login(self, name, pin):
        user = self.users.get(name)
        if user and user.verify_pin(pin):
            self.login_attempts[name] = 0  # Reset attempts on successful login
            print(f"Welcome, {name}!")
            return user
        else:
            self.login_attempts[name] = self.login_attempts.get(name, 0) + 1
            print("Invalid name or PIN.")
            if self.login_attempts[name] >= 3:
                print(f"Account locked for {name} due to too many failed attempts.")
            return None

# Main function for interacting with the ATM
def main():
    atm = ATM()

    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter your name: ")
            pin = input("Create a 4-digit PIN: ")
            atm.create_user(name, pin)

        elif choice == '2':
            name = input("Enter your name: ")
            pin = input("Enter your PIN: ")
            user = atm.login(name, pin)

            if user:
                while True:
                    print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Transaction History\n5. Logout")
                    action = input("Choose an action: ")

                    if action == '1':
                        print(f"Current balance: ${user.balance}")

                    elif action == '2':
                        try:
                            amount = float(input("Enter amount to deposit: "))
                            user.deposit(amount)
                        except ValueError:
                            print("Please enter a valid number.")

                    elif action == '3':
                        try:
                            amount = float(input("Enter amount to withdraw: "))
                            user.withdraw(amount)
                        except ValueError:
                            print("Please enter a valid number.")

                    elif action == '4':
                        user.print_transactions()

                    elif action == '5':
                        print("Logged out.")
                        break

                    else:
                        print("Invalid option. Please try again.")

        elif choice == '3':
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
