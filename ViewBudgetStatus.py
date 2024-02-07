# Code:
from colorama import Fore
from CategorySummary import get_expense_categories_and_totals, get_income_sources_and_totals
from BudgetStatus import calculate_budget_status
from Global import category_budgets, expenses_list, income_list

# Code:

def view_budget_status():
    """
    Displays the budget status, including category-wise and overall budget status.
    """
    # Calculate total expenses and income
    total_expenses = sum(float(entry.amount) for entry in expenses_list)
    total_income = sum(float(entry.amount) for entry in income_list)

    # Calculate category-wise budget status
    category_budget_status = {}
    for category, budget_amount in category_budgets.items():
        total_category_expenses = sum(float(entry.amount) for entry in expenses_list if entry.category == category)
        difference = budget_amount - total_category_expenses
        status, _ = calculate_budget_status(budget_amount, total_category_expenses)
        category_budget_status[category] = (status, difference)

    # Calculate overall budget status
    overall_difference = total_income - total_expenses
    overall_budget_status, _ = calculate_budget_status(sum(category_budgets.values()), total_expenses)

    # Print category-wise budget status
    print("\nCategory Budget Status:")
    for category, (status, difference) in category_budget_status.items():
        if difference >= 0:
            print(f"{category}: ${total_category_expenses:.2f} | Budget Status: {Fore.GREEN}Under Budget ({difference:.2f} difference){Fore.RESET}")
        else:
            print(f"{category}: ${total_category_expenses:.2f} | Budget Status: {Fore.RED}Over Budget ({abs(difference):.2f} difference){Fore.RESET}")

    # Print overall budget status
    if overall_difference >= 0:
        print(f"\nOverall Budget: ${total_income:.2f} | Overall Budget Status: {Fore.GREEN}Under Budget ({overall_difference:.2f} difference){Fore.RESET}")
    else:
        print(f"\nOverall Budget: ${total_income:.2f} | Overall Budget Status: {Fore.RED}Over Budget ({abs(overall_difference):.2f} difference){Fore.RESET}")
