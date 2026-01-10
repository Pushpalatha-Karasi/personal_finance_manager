import csv
import os
import shutil
from src.expense import Expense


class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.backup_folder = "backup"
        self.backup_file = os.path.join(self.backup_folder, "expenses_backup.csv")

    # ---------------- LOAD EXPENSES ---------------- #

    def load_expenses(self):
        expenses = []

        if not os.path.exists(self.filename):
            return expenses

        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header

            for row in reader:
                expense = Expense(
                    date=row[0],
                    category=row[1],
                    amount=float(row[2]),
                    description=row[3]
                )
                expenses.append(expense)

        return expenses

    # ---------------- SAVE EXPENSE ---------------- #

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

    # ---------------- BACKUP ---------------- #

    def create_backup(self):
        os.makedirs(self.backup_folder, exist_ok=True)
        shutil.copy(self.filename, self.backup_file)
