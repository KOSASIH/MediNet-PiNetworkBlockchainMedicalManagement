import re

def is_valid_email(email):
    # Check if email is valid
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def is_valid_phone_number(phone):
    # Check if phone number is valid
    return bool(re.match(r"^\+?[\d\s()-]*$", phone))

def is_valid_date(date, format="%Y-%m-%d"):
    # Check if date is valid
    try:
        return bool(datetime.strptime(date, format))
    except ValueError:
        return False

def is_valid_transaction(transaction):
    # Check if transaction is valid
    # This would depend on the specifics of your system
    pass
