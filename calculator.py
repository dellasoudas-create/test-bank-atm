# ============================================================
# Python Calculator
# Author: Haris Dellasoudas
# Description:
# A simple calculator app built with Python.
# It supports addition, subtraction, multiplication,
# division, power and percentage calculation.
# ============================================================


def show_menu():
    print("\n========== PYTHON CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Percentage")
    print("7. Exit")
    print("=======================================")


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add():
    first_number = get_number("Enter first number: ")
    second_number = get_number("Enter second number: ")
    result = first_number + second_number
    print(f"Result: {first_number} + {second_number} = {result}")


def subtract():
    first_number = get_number("Enter first number: ")
    second_number = get_number("Enter second number: ")
    result = first_number - second_number
    print(f"Result: {first_number} - {second_number} = {result}")


def multiply():
    first_number = get_number("Enter first number: ")
    second_number = get_number("Enter second number: ")
    result = first_number * second_number
    print(f"Result: {first_number} × {second_number} = {result}")


def divide():
    first_number = get_number("Enter first number: ")
    second_number = get_number("Enter second number: ")

    if second_number == 0:
        print("Error: You cannot divide by zero.")
        return

    result = first_number / second_number
    print(f"Result: {first_number} / {second_number} = {result}")


def power():
    first_number = get_number("Enter base number: ")
    second_number = get_number("Enter exponent: ")
    result = first_number ** second_number
    print(f"Result: {first_number} ^ {second_number} = {result}")


def percentage():
    number = get_number("Enter the number: ")
    percent = get_number("Enter the percentage: ")
    result = number * percent / 100
    print(f"Result: {percent}% of {number} = {result}")


def main():
    while True:
        show_menu()
        choice = input("Choose an option from 1 to 7: ")

        if choice == "1":
            add()

        elif choice == "2":
            subtract()

        elif choice == "3":
            multiply()

        elif choice == "4":
            divide()

        elif choice == "5":
            power()

        elif choice == "6":
            percentage()

        elif choice == "7":
            print("\nThank you for using Python Calculator. Goodbye!")
            break

        else:
            print("Invalid option. Please choose from 1 to 7.")


if __name__ == "__main__":
    main()