import json
import os
from datetime import datetime

home_directory = os.path.expanduser("~")
expense_data_file = os.path.join(home_directory, 'expenses.json')

def load_expense_data():
    try:
        with open(expense_data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_expense_data(data):
    with open(expense_data_file, 'w') as file:
        json.dump(data, file, indent=4)

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., food, transportation, entertainment): ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a brief description: ")

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }

    data = load_expense_data()
    if date not in data:
        data[date] = []
    data[date].append(expense)
    save_expense_data(data)
    print("Expense added successfully!")

def view_summary():
    data = load_expense_data()
    monthly_summary = {}
    category_summary = {}

    for date, expenses in data.items():
        month = date[:7]  # Extracting YYYY-MM
        if month not in monthly_summary:
            monthly_summary[month] = 0
        for expense in expenses:
            monthly_summary[month] += expense['amount']
            if expense['category'] not in category_summary:
                category_summary[expense['category']] = 0
            category_summary[expense['category']] += expense['amount']

    print("\nMonthly Summary:")
    for month, total in monthly_summary.items():
        print(f"{month}: ${total:.2f}")

    print("\nCategory-wise Summary:")
    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")

def main_menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

try:
    main_menu()
except Exception as e:
    print(f"An error occurred: {e}")


