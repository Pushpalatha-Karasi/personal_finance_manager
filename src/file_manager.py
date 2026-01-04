import csv
import os
import shutil
from .expense import Expense

class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.backup_file = "backup/expenses_backup.csv"

    def load_expenses(self):
        expenses = []

        if not os.path.exists(self.filename):
            return expenses

        with open(self.filename, "r") as file:
            reader = csv.reader(file)
            header = next(reader, None)

            for row in reader:
                expenses.append(
                    Expense(row[0], row[1], float(row[2]), row[3])
                )

        return expenses

    def save_expense(self, expense):
        file_exists = os.path.exists(self.filename)

        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["date", "category", "amount", "description"])

            writer.writerow([
                expense.date,
                expense.category,
                expense.amount,
                expense.description
            ])

        self.create_backup()

    def create_backup(self):
        os.makedirs("backup", exist_ok=True)
        shutil.copy(self.filename, self.backup_file)
