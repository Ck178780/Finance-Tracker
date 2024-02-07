# Imports:
import datetime

# Code:

class Expense:
    """
    Represents an individual expense.

    Attributes:
    - date (str): The date of the expense in the format YYYY-MM-DD.
    - category (str): The category of the expense.
    - amount (float): The amount spent on the expense.
    - description (str): A description of the expense.
    """

    def __init__(self, date, category, amount, description):
        """
        Initializes an Expense object.

        Parameters:
        - date (str): The date of the expense in the format YYYY-MM-DD.
        - category (str): The category of the expense.
        - amount (float): The amount spent on the expense.
        - description (str): A description of the expense.
        """
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        """
        Returns a string representation of the Expense object.

        Returns:
        str: A formatted string containing expense details.
        """
        return f"{self.date} | {self.category} | ${self.amount} | {self.description}"

def validate_date(date_string):
    """
    Validates if a given date string is in the format YYYY-MM-DD.

    Parameters:
    - date_string (str): The date string to validate.

    Returns:
    bool: True if the date string is in the correct format, False otherwise.
    """
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_amount(amount):
    """
    Validates if a given amount is a valid float.

    Parameters:
    - amount (str): The amount to validate.

    Returns:
    bool: True if the amount is a valid float, False otherwise.
    """
    try:
        float(amount)
        return True
    except ValueError:
        return False

def get_expense_input():
    """
    Collects user input for expense details with real-time validation.

    Returns:
    Expense: An Expense object containing user-provided expense details.
    """
    date = input("Enter expense date (YYYY-MM-DD): ")
    while not validate_date(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        date = input("Enter expense date (YYYY-MM-DD): ")

    category = input("Enter expense category: ")

    amount = input("Enter expense amount: ")
    while not validate_amount(amount):
        print("Invalid amount. Please enter a valid number.")
        amount = input("Enter expense amount: ")

    description = input("Enter expense description: ")

    return Expense(date, category, amount, description)
