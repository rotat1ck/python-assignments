import re
def isValidPassword(password):
    if re.match(r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[.,!?;:-])[a-zA-Z\d.,!?;:-]{8,}$", password):
        return True
    else:
        return False
    
print(isValidPassword("Short1!4545"))

def isValidPhone(phone):
    pattern = r"\+7 \d{3} \d{3} \d{2} \d{2}|8 \(\d{3}\) \d{3}-\d{2}-\d{2}|8\d{10}|\+7-\d{3}-\d{3}-\d{2}-\d{2}"
    
    if re.match(pattern, phone):
        return "Номер корректный"
    else:
        return "Неккоректный номер"
    
print(isValidPhone("8 (999) 123-45-67"))