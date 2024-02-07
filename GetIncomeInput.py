# Imports:
from GetUserInput import get_user_input 
from Income import Income, validate_income_date, validate_income_amount

# Code:
def get_income_input():
    """
    Collects user input for income details with real-time validation.

    Returns:
    Income: An Income object containing user-provided income details.
    """
    date = get_user_input("Enter income date (YYYY-MM-DD): ")
    while not validate_income_date(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        date = get_user_input("Enter income date (YYYY-MM-DD): ")

    source = get_user_input("Enter income source: ")

    amount = get_user_input("Enter income amount: ")
    while not validate_income_amount(amount):
        print("Invalid amount. Please enter a valid number.")
        amount = get_user_input("Enter income amount: ")

    description = get_user_input("Enter income description: ")

    return Income(date, source, amount, description)