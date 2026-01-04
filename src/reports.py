from .utils import clean_text

class Reports :
    
    @staticmethod
    def total_expense(expenses):
        total = 0 
        for e in expenses :
            total += e.amount
        return total
        
    
    @staticmethod 
    def category_wise_expense(expenses):
        category_totals = {}
        
        for e in expenses:
            category = clean_text(e.category)
            amount = e.amount
            
            if category in category_totals :
                category_totals[category] += amount
                
            else :
                category_totals[category] = amount
                
        return category_totals
    
    @staticmethod
    def average_expense(expenses):
        if len(expenses)==0 :
            return 0 
        total = 0
        for e in expenses :
            total += e.amount
            average = total /len(expenses)
        return round(average)
    
    @staticmethod
    def monthly_expenses(expenses):
        
        monthly_totals = {}
        
        for e in expenses:
            month = e.date[: 7]
            
            if month in monthly_totals :
                monthly_totals[month] += e.amount
            
            else :
                monthly_totals[month] = e.amount

        return monthly_totals
    
    
    @staticmethod
    def filter_by_category(expenses, category):
        filtered = []
        
        for e in expenses :
            if clean_text(e.category) == clean_text(category) :
                filtered.append(e)
                
        return filtered
            
    