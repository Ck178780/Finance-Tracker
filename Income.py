# Imports:
import datetime

# Code:

class Income:
    """
    Represents an individual income entry.

    Attributes:
    - date (str): The date of the income in the format YYYY-MM-DD.
    - source (str): The source of the income.
    - amount (float): The amount of the income.
    - description (str): A description of the income.
    """

    def __init__(self, date, source, amount, description):
        """
        Initializes an Income object.

        Parameters:
        - date (str): The date of the income in the format YYYY-MM-DD.
        - source (str): The source of the income.
        - amount (float): The amount of the income.
        - description (str): A description of the income.
        """
        self.date = date
        self.source = source
        self.amount = amount
        self.description = description

    def __str__(self):
        """
        Returns a string representation of the Income object.

        Returns:
        str: A formatted string containing income details.
        """
        return f"{self.date} | {self.source} | ${self.amount} | {self.description}"

def validate_income_date(date_string):
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

def validate_income_amount(amount):
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

def get_income_input():
    """
    Collects user input for income details with real-time validation.

    Returns:
    Income: An Income object containing user-provided income details.
    """
    date = input("Enter income date (YYYY-MM-DD): ")
    while not validate_income_date(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        date = input("Enter income date (YYYY-MM-DD): ")

    source = input("Enter income source: ")

    amount = input("Enter income amount: ")
    while not validate_income_amount(amount):
        print("Invalid amount. Please enter a valid number.")
        amount = input("Enter income amount: ")

    description = input("Enter income description: ")

    return Income(date, source, amount, description)
