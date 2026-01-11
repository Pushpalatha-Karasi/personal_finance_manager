from src.expense import Expense
from src.file_manager import FileManager
from src.utils import clean_text, validate_amount, validate_date


class ExpenseManager:
    def __init__(self):
        self.file_manager = FileManager("data/expenses.csv")
        self.expenses = self.file_manager.load_expenses()

    # 🔹 MAIN METHOD (Very clean)
    def add_expense(self):
        date = self._get_valid_date()
        category = self._get_category()
        amount = self._get_valid_amount()
        description = self._get_description()

        expense = Expense(date, category, amount, description)
        self.expenses.append(expense)
        self.file_manager.save_expense(expense)

        print("✅ Expense added successfully")

    # ---------------- HELPER METHODS ---------------- #

    def _get_valid_date(self):
        while True:
            date = input("Date (YYYY-MM-DD): ").strip()
            if validate_date(date):
                return date
            print("❌ Invalid date format. Try again.")

    def _get_category(self):
        raw_category = input("Category: ")
        return clean_text(raw_category)

    def _get_valid_amount(self):
         while True:
            raw_amount = input("Amount: ")
            amount = validate_amount(raw_amount)
            if amount is not None:
                    return amount
                    print("❌ Invalid amount. Enter a positive number.")

    def _get_description(self):
            raw_description = input("Description: ")
            return clean_text(raw_description)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses yet")
            return
        for e in self.expenses:
            e.display()

    
    def filter_by_category(self):
        category = clean_text(input("Enter category: "))
            
        filtered_expenses = [
        e for e in self.expenses if e.category == category
        ]

        if not filtered_expenses:
            print("No expenses found for this category")
            return

        for expense in filtered_expenses:
            expense.display()
