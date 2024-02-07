# Imports:
from GetUserInput import get_user_input
from Expenses import Expense, validate_date as validate_expense_date, validate_amount as validate_expense_amount

# Code:

def get_expense_input():
    """
    Collects user input for expense details with real-time validation.

    Returns:
    Expense: An Expense object containing user-provided expense details.
    """
    date = get_user_input("Enter expense date (YYYY-MM-DD): ")
    while not validate_expense_date(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        date = get_user_input("Enter expense date (YYYY-MM-DD): ")

    category = get_user_input("Enter expense category: ")

    amount = get_user_input("Enter expense amount: ")
    while not validate_expense_amount(amount):
        print("Invalid amount. Please enter a valid number.")
        amount = get_user_input("Enter expense amount: ")

    description = get_user_input("Enter expense description: ")

    return Expense(date, category, amount, description)