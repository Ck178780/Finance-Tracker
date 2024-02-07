# Imports:
import csv
from Expenses import Expense
from Income import Income

# Code:

def export_to_csv(entries, filename):
    """
    Exports the given list of entries to a CSV file.

    Parameters:
    - entries (list): List of Expense or Income objects to be exported.
    - filename (str): Name of the CSV file to export to.

    Returns:
    None
    """
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Type', 'Date', 'Category/Source', 'Amount', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            if isinstance(entry, Expense):
                entry_type = 'Expense'
                category_or_source = entry.category
            elif isinstance(entry, Income):
                entry_type = 'Income'
                category_or_source = entry.source
            writer.writerow({'Type': entry_type, 'Date': entry.date, 'Category/Source': category_or_source, 'Amount': entry.amount, 'Description': entry.description})
