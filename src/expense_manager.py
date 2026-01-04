from .expense import Expense
from .file_manager import FileManager
from .reports import Reports
from .utils import clean_text, validate_amount, validate_date

class ExpenseManager:
    def __init__(self):
        self.file_manager = FileManager("data/expenses.csv")
        self.expenses = self.file_manager.load_expenses()

    def add_expense(self):
        
        #-------------Date---------------
        while True:    
            date = input("Date (YYYY-MM-DD): ").strip()
            if validate_date(date):
                break
                print("Invalid date format") 
               
               #-------------Category-----------
        raw_category = input("Category: ")
        category = clean_text(raw_category)
        
        #------------AMOUNT---------------
        
        while True:
            
            raw_amount = input("Amount: ")
            amount = validate_amount(raw_amount)
        
            if amount is not None:
                break
                print("Invalid amount try again")
        
        #-------------Description ------------
        raw_description = input("Description: ")
        description = clean_text(raw_description)
        
#-------------------Create Expense ----------------
        expense = Expense(date, category, amount, description)
        self.expenses.append(expense)
        self.file_manager.save_expense(expense)

        print("✅ Expense added successfuly ")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses yet")
            return
        for e in self.expenses:
            e.display()
