# Imports:
from GetUserInput import get_user_input
from SearchEntries import search_entries
from GetExpenseInput import validate_expense_date
from GetIncomeInput import validate_income_date
from Expenses import Expense
from Income import Income

# Code:

def edit_entry(entries):
    """
    Allows the user to search for and edit an existing entry.
    """
    matching_entries = search_entries(entries)

    if not matching_entries:
        print("No matching entries found.")
        return

    print("\nMatching Entries:")
    for index, entry in enumerate(matching_entries, start=1):
        print(f"{index}. {entry}")

    entry_to_edit = None

    while entry_to_edit is None:
        entry_selection = get_user_input("Select an entry to edit (enter date, source, or amount): ").lower()

        for entry in matching_entries:
            if isinstance(entry, Expense):
                if entry_selection in [entry.date, entry.category.lower()]:
                    entry_to_edit = entry
                    break
                elif entry_selection == entry.amount:
                    entry_to_edit = entry
                    break
            elif isinstance(entry, Income):
                if entry_selection in [entry.date, entry.source.lower()]:
                    entry_to_edit = entry
                    break
                elif entry_selection == entry.amount:
                    entry_to_edit = entry
                    break

        if entry_to_edit is None:
            print("Invalid selection. Please enter a valid date, source, or amount.")

    print(f"\nEditing Entry:")
    print(entry_to_edit)

    new_date = get_user_input("Enter new date (YYYY-MM-DD): ")
    while not validate_expense_date(new_date) and not validate_income_date(new_date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        new_date = get_user_input("Enter new date (YYYY-MM-DD): ")

    new_amount = get_user_input("Enter new amount: ")
    new_description = get_user_input("Enter new description: ")

    # Update the entry with the new information:
    entry_to_edit.date = new_date
    entry_to_edit.amount = new_amount
    entry_to_edit.description = new_description

    if isinstance(entry_to_edit, Expense):
        new_category = get_user_input("Enter new category: ")
        entry_to_edit.category = new_category
    elif isinstance(entry_to_edit, Income):
        new_source = get_user_input("Enter new source: ")
        entry_to_edit.source = new_source

    print("Entry updated successfully.")
