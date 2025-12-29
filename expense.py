
class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.description = description

    def display(self):
        print(f"{self.date} | {self.category} | ₹{self.amount} | {self.description}")

