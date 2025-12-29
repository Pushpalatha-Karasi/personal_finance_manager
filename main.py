
from expense_manager import ExpenseManager
from reports import Reports

def main():
    manager = ExpenseManager()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expense")
        print("4.Category_wise_expense")
        print("5.Average_expense")
        print("6. Monthly Reports")
        print("7.Filter expenses by category ")
        print("8.Exit")

        choice = input("Choose: ")

        if choice == "1":
            manager.add_expense()
        elif choice == "2":
            manager.view_expenses()
        elif choice == "3":
            total = Reports.total_expense(manager.expenses)
            print(f"Total Expense:{total}")   
            
        elif choice == "4" :
            category_totals = Reports.category_wise_expense(manager.expenses)
            print("Category_wise_expense")
            for category , totals in category_totals.items():
                print(f"{category}:{totals}")    
                
        elif choice == "5" :
            average_expense = Reports.average_expense(manager.expenses)
            print(f"Your Average expense is {average_expense} Rupees")
            
        elif choice == "6":
            monthly_totals = Reports.monthly_expenses(manager.expenses)
            for month , totals in monthly_totals.items() : 
                print(month ,":" ,totals)
                
        elif choice == "7" :
            category = input("Enter category to filter")
            results = Reports.filter_by_category(manager.expenses,category)
            
            if not results :
                print("No Expenses found for this category")
                
            else:
                
                for e in results :
                    print(f"{e.date} | {e.category} | {e.amount} | {e.description}")
                    
        elif choice == "8":
            print("Bye 👋")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
