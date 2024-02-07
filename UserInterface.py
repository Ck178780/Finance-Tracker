# Imports:
from CategorySummary import view_category_summary
from colorama import init
from ExportCSV import export_to_csv
from DeleteAllData import delete_all_data
from ViewBudgetStatus import view_budget_status
from GetUserInput import get_user_input
from GetExpenseInput import get_expense_input
from GetIncomeInput import get_income_input
from SetCategoryBudget import set_category_budget
from EditEntry import edit_entry
from ViewEntries import view_entries
from DeleteEntry import delete_entry
from Global import expenses_list, income_list


# Code:

# Initialize colorama
init(autoreset=True)

def show_menu():
    """
    Displays the main menu of the Finance Tracker.
    This function prints the available options for the user in the command-line interface.
    """
    print("Finance Tracker Menu:")
    print("1. Add Expense")
    print("2. Add Income")
    print("3. View Expenses")
    print("4. View Income")
    print("5. View Category Summary")
    print("6. Set Category Budget")
    print("7. View Budget Status")
    print("8. Edit an Entry")
    print("9. Export Data to CSV")
    print("10. Delete Expense Entry")
    print("11. Delete Income Entry")
    print("12. Exit Finance Tracker")
    print("13. Clear all data.")

# Terminal UI Code:
if __name__ == "__main__":
    while True:
        show_menu()
        choice = get_user_input("Enter your choice: ")

        if choice == '1':
            expense = get_expense_input()
            expenses_list.append(expense)
            print("Expense Details:")
            print(expense)
            
        elif choice == '2':
            income = get_income_input()
            income_list.append(income)
            print("Income Details:")
            print(income)
            
        elif choice == '3':
            view_entries(expenses_list, 'Expense')
   
        elif choice == '4':
            view_entries(income_list, 'Income')

        elif choice == '5':
            view_category_summary(expenses_list, income_list)

        elif choice == '6':
            set_category_budget()

        elif choice == '7':
            view_budget_status()

        elif choice == '8':
            edit_entry(expenses_list + income_list)

        elif choice == '9':
            csv_filename = input("Enter filename for .csv export: ")
            combined_entries = expenses_list + income_list
            export_to_csv(combined_entries, csv_filename)
            print("Expenses and income exported to CSV successfully.")
     
        elif choice == '10':
            delete_entry(expenses_list)
            
        elif choice == '11':
            delete_entry(income_list)
    
        elif choice == '12':
            print("Exiting the Finance Tracker. Goodbye!")
            break
        
        elif choice == '13':
            delete_all_data()

        else:
            print("Invalid choice. Please choose a valid option.")
