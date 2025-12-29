import csv
from expense import Expense

class FileManager:

    def __init__(self, filename):
        self.filename = filename

    def load_expenses(self):
        expenses = []
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                next(reader, None)
                
                for row in reader:
                    expenses.append(
                        Expense(row[0], row[1], row[2], row[3])
                    )
        except FileNotFoundError:
            pass

        return expenses

    def save_expense(self, expense):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                expense.date,
                expense.category,
                expense.amount,
                expense.description
            ])
