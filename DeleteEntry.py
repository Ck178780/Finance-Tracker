# Imports:
from GetUserInput import get_user_input
from SearchEntries import search_entries
from Expenses import Expense
from Income import Income

def delete_entry(entries):
    """
    Allows the user to search for and delete an existing entry.

    Parameters:
    - entries (list): List of Expense or Income objects.

    Returns:
    None
    """
    matching_entries = search_entries(entries)

    if not matching_entries:
        print("No matching entries found.")
        return

    print("\nMatching Entries:")
    for index, entry in enumerate(matching_entries, start=1):
        print(f"{index}. {entry}")

    entry_to_delete = None

    while entry_to_delete is None:
        entry_selection = get_user_input("Select an entry to delete (enter date, source, or amount): ").lower()

        for entry in matching_entries:
            if isinstance(entry, Expense):
                if entry_selection in [entry.date, entry.category.lower()]:
                    entry_to_delete = entry
                    break
                elif entry_selection == entry.amount:
                    entry_to_delete = entry
                    break
            elif isinstance(entry, Income):
                if entry_selection in [entry.date, entry.source.lower()]:
                    entry_to_delete = entry
                    break
                elif entry_selection == entry.amount:
                    entry_to_delete = entry
                    break

        if entry_to_delete is None:
            print("Invalid selection. Please enter a valid date, source, or amount.")

    # Remove the entry from the list
    entries.remove(entry_to_delete)
    print("Entry deleted successfully.")
