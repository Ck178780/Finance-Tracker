Finance Tracker Application:

The application allows users to easily enter budget details and helps users to keep information accurate with real time validation. If for example a user is in a rush and enters the incorrect date or time the userinterface would inform users thereof immediately and not crash due to an error.

 Finance Tracker Menu:
    1. Add Expense
    2. Add Income
    3. View Expenses
    4. View Income
    5. View Category Summary
    6. Set Category Budget
    7. View Budget Status
    8. Edit an Entry
    9. Export Data to CSV
    10. Delete Expense Entry
    11. Delete Income Entry
    12. Exit Finance Tracker
    13. Clear all data.

Colour: Noticed the terminal can get confusing with income and expenses numbers being the same colour. Adjusted the code to have all 'under budget' printed in green and 'over budget' printed in red. Using the 'colorama' library.

Validation: Double checked confirm that a user can't input strange dates e.g., 2024/02/05, 2024-02-31, 2024-13-05. Users can input e.g., 2024-02-29

Editing: When a user needs to edit an entry they have are able to search and view all entries in a category and then, select by date which entry they want to modify. If there are two or more entries with the same date and category the user can select an entry through input of the desired entry to modify amount. 

Value: To add extra value to the user, add the option to export the entries made in the application to a pdf or csv file which user can then send/give to their accountants if needed or keep detailed records of their finances. 

Delete all data: The user has the option to delete/erase all data. Added safety feature which promts the user for confirmation of "Yes, I am sure." to erase all data, if user input differs from that suggested in the prompt nothing will be deleted and the error handled safely. If a user accedentitally selected this option they are prompted to enter "No" to cancel the operation.


