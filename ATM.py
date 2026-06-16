# ============================================================
# ATM Simulation
# Author: Haris Dellasoudas
# Description:
# A simple ATM simulation app with PIN login, balance check,
# deposit, withdrawal and PIN change.
# ============================================================


def show_menu():
    print("\n========== TEST BANK ATM ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")
    print("===================================")


def check_balance(balance):
    print(f"\nYour current balance is: €{balance:.2f}")


def deposit_money(balance):
    try:
        amount = float(input("\nEnter amount to deposit: €"))

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return balance

        balance += amount
        print(f"Deposit successful. New balance: €{balance:.2f}")
        return balance

    except ValueError:
        print("Invalid amount. Please enter a number.")
        return balance


def withdraw_money(balance):
    try:
        amount = float(input("\nEnter amount to withdraw: €"))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return balance

        if amount > balance:
            print("Insufficient balance.")
            return balance

        balance -= amount
        print(f"Withdrawal successful. New balance: €{balance:.2f}")
        return balance

    except ValueError:
        print("Invalid amount. Please enter a number.")
        return balance


def change_pin(current_pin):
    old_pin = input("\nEnter your current PIN: ")

    if old_pin != current_pin:
        print("Incorrect current PIN.")
        return current_pin

    new_pin = input("Enter your new 4-digit PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must be exactly 4 digits.")
        return current_pin

    confirm_pin = input("Confirm your new PIN: ")

    if new_pin != confirm_pin:
        print("PIN confirmation does not match.")
        return current_pin

    print("PIN changed successfully.")
    return new_pin


def login(pin):
    attempts = 3

    while attempts > 0:
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            print("\nLogin successful. Welcome to TEST BANK!")
            return True

        attempts -= 1
        print(f"Wrong PIN. Attempts left: {attempts}")

    print("\nToo many failed attempts. Card blocked.")
    return False


def main():
    pin = "1234"
    balance = 5000.00

    print("================================")
    print("Welcome to TEST BANK ATM")
    print("================================")

    is_logged_in = login(pin)

    if not is_logged_in:
        return

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit_money(balance)

        elif choice == "3":
            balance = withdraw_money(balance)

        elif choice == "4":
            pin = change_pin(pin)

        elif choice == "5":
            print("\nThank you for using TEST BANK ATM. Goodbye!")
            break

        else:
            print("Invalid option. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()