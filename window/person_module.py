from persian_tools import national_id, phone_number, plate, bill
from persian_tools.bank import card_number

def check_national_id(num):
    if national_id.validate(num):
        return num
    else:
        raise ValueError("کد ملی نامعتبر است")

def check_phone_number(num):
    if phone_number.validate(num):
        return num
    else:
        raise ValueError("شماره تلفن نامعتبر است")

def check_card_number(num):
    if card_number.validate(num):
        return num
    else:
        raise ValueError("شماره کارت نامعتبر است")

def check_plate_number(num):
    if plate.is_valid(num):
        return num
    else:
        raise ValueError("شماره پلاک نامعتبر است")

def check_bill_id(bill_id):
    if len(bill_id) == 13 and bill_id.isdigit():
        return bill_id
    else:
        raise ValueError("شناسه قبض نامعتبر است")