# Imports:
from GetUserInput import get_user_input 
from Global import category_budgets

# Code:

def set_category_budget():
    """
    Allows the user to set a budget for a specific category.
    """
    category = get_user_input("Enter category for budget: ")
    budget_amount = float(get_user_input("Enter budget amount for the category: "))
    category_budgets[category] = budget_amount
    print(f"Budget set for {category} category: ${budget_amount:.2f}")