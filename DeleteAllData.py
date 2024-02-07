# Imports:
from GetUserInput import get_user_input

def delete_all_data():
    """
    Deletes all data from the application after user confirmation.
    """
    global expenses_list, income_list, category_budgets
    confirmation = get_user_input("Are you sure you want to delete all data? (Type 'Yes, I am sure.' to confirm, or 'No' to cancel): ")
    if "yes, i am sure." in confirmation.lower():
        expenses_list = []
        income_list = []
        category_budgets = {}
        print("All data deleted successfully.")
    elif confirmation.lower() == "no":
        print("Operation cancelled. No data was deleted.")
    else:
        print("Invalid input. Operation cancelled. No data was deleted.")