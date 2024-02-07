def calculate_budget_status(budget_amount, total_amount):
    """
    Calculates and returns the budget status (more, less, or equal) and the difference.

    Parameters:
    - budget_amount (float): The budget amount.
    - total_amount (float): The total amount of expenses or income.

    Returns:
    tuple: A tuple containing the budget status (str) and the difference (float).
    """
    difference = budget_amount - total_amount

    if difference > 0:
        status = "Over Budget"
    elif difference < 0:
        status = "Under Budget"
    else:
        status = "On Budget"

    return status, abs(difference)
