import re

def normalize_phone(phone_number: str):
    phone = re.sub(r"[^\d+]", "", phone_number)

    if phone.startswith("+"):
        return phone
    elif phone.startswith("380"):
        return "+" + phone
    else:
        return "+38" + phone