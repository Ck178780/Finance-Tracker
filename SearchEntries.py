# Imports:
from GetUserInput import get_user_input
from Expenses import Expense
from Income import Income

# Code:

def search_entries(entries):
    """
    Allows the user to search for entries by date, category, or description.
    Returns a list of matching entries.

    Parameters:
    - entries (list): List of Expense or Income objects to search within.

    Returns:
    list: List of matching entries.
    """
    search_term = get_user_input("Enter search term (date, category, or description): ").lower()
    matching_entries = []

    for entry in entries:
        if isinstance(entry, Expense):
            if search_term in [entry.date, entry.category.lower(), entry.description.lower()]:
                matching_entries.append(entry)
        elif isinstance(entry, Income):
            if search_term in [entry.date, entry.source.lower(), entry.description.lower()]:
                matching_entries.append(entry)

    return matching_entries
