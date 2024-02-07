# Imports:
import unittest
from unittest.mock import patch
from io import StringIO
from UserInterface import show_menu
from GetUserInput import get_user_input

# Code:

class TestUserInterface(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_show_menu(self, mock_input):
        expected_output = (
            "Finance Tracker Menu:\n"
            "1. Add Expense\n"
            "2. Add Income\n"
            "3. View Expenses\n"
            "4. View Income\n"
            "5. View Category Summary\n"
            "6. Set Category Budget\n"
            "7. View Budget Status\n"
            "8. Edit an Entry\n"
            "9. Export Data to CSV\n"
            "10. Delete Expense Entry\n"
            "11. Delete Income Entry\n"
            "12. Exit Finance Tracker\n"
            "13. Clear all data."
        )
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            show_menu()
            actual_output = mock_stdout.getvalue()
            actual_lines = actual_output.splitlines()
            expected_lines = expected_output.splitlines()
            self.assertEqual(actual_lines, expected_lines)

    @patch('builtins.input', side_effect=['test'])
    def test_get_user_input(self, mock_input):
        expected_output = 'test'
        user_input = get_user_input('Enter your choice: ')
        self.assertEqual(user_input, expected_output)

if __name__ == '__main__':
    unittest.main()
