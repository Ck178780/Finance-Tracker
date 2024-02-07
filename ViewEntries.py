# Imports:
from colorama import Fore
from datetime import datetime

# Code:

def view_entries(entries, entry_type):
    """
    Displays the list of entries in descending order by date.

    Parameters:
    - entries (list): List of Expense or Income objects.
    - entry_type (str): A string indicating the type of entry ('Expense' or 'Income').
    """
    sorted_entries = sorted(entries, key=lambda x: datetime.strptime(x.date, "%Y-%m-%d"), reverse=True)

    print(f"\n{entry_type} List:")
    for index, entry in enumerate(sorted_entries, start=1):
        if entry_type == 'Expense':
            print(f"{Fore.RED}{index}. {entry}")
        elif entry_type == 'Income':
            print(f"{Fore.GREEN}{index}. {entry}")