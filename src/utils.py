
def clean_text(text):
    return text.strip().lower()

def validate_amount(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            return None
        return amount
    except ValueError :
        return None
    
    
def validate_date(date):
    if len(date) != 10:
        return False
    if date[4] != "-" or date[7] != "-":
        return False
    return True

        