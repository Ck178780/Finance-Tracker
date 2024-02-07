# Imports:
from Expenses import Expense
from Income import Income

# Code:

def get_expense_categories_and_totals(expenses):
    """
    Calculates and returns a dictionary of expense categories and the totals.

    Parameters:
    - expenses (list): A list of Expense objects.

    Returns:
    dict: A dictionary where keys are expense categories and values are the total amounts.
    """
    category_totals = {}

    for expense in expenses:
        category = expense.category
        amount = float(expense.amount)

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals

def get_income_sources_and_totals(income_entries):
    """
    Calculates and returns a dictionary of income sources and their totals.

    Parameters:
    - income_entries (list): A list of Income objects.

    Returns:
    dict: A dictionary where keys are income sources and values are the total amounts.
    """
    source_totals = {}

    for income_entry in income_entries:
        source = income_entry.source
        amount = float(income_entry.amount)

        if source in source_totals:
            source_totals[source] += amount
        else:
            source_totals[source] = amount

    return source_totals

def view_category_summary(expenses, income_entries):
    """
    Displays the summary of expense and income categories along with their respective totals.

    Parameters:
    - expenses (list): A list of Expense objects.
    - income_entries (list): A list of Income objects.
    """
    expense_category_totals = get_expense_categories_and_totals(expenses)
    income_source_totals = get_income_sources_and_totals(income_entries)

    print("\nExpense Category Summary:")
    for category, total in expense_category_totals.items():
        print(f"{category}: ${total:.2f}")

    print("\nIncome Source Summary:")
    for source, total in income_source_totals.items():
        print(f"{source}: ${total:.2f}")


