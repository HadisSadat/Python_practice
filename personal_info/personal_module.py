from persian_tools import national_id, phone_number, plate, bill
from persian_tools.bank import card_number

def show_menu():
    print("1) National ID")
    print("2) Phone Number")
    print("3) Card Number")
    print("4) Plate Number")
    print("5) bill ID")
    print("0) Exit")
    return int(input("Choose Option : "))

def check_national_id():
    num= input("Enter National ID : ")
    if national_id.validate(num):
        print("Valid")
        info = national_id.find_place(num)
        print("استان : " ,info["province"])
        print(" شهر : " ,info["city"])
    else:
        print("Invalid")

def check_phone_number():
    num = input("Enter Phone Number : ")
    if phone_number.validate(num):
        print("Valid")
        info = phone_number.operator_data(num)
        print("اپراتور:", info["operator"])
        print("محدوده:", info["province"])
    else:
        print("Invalid")


def check_card_number():
    num = input("Enter Card Number : ")
    if card_number.validate(num):
        print("Valid")
        info = card_number.bank_data(num)
        print("نام : " ,info["persian_name"])
        print("شبا : " ,info["sheba_code"])
    else:
        print("Invalid")

def check_plate_number():
    num = input("Enter Plate Number : ")
    if plate.is_valid(num):
        print("Valid")
        info = plate.get_info(num)
        print("استان : " ,info["province"])
        print("دسته بندی : " ,info["category"])
    else:
        print("Invalid")


def check_bill_id():
    bill_id = input("Enter Bill ID: ")
    payment_id = input("Enter Payment ID: ")

    information = bill.get_detail(
        bill_id=int(bill_id),
        payment_id=int(payment_id)
    )

    if information["is_valid"]:
        print("Valid")
        print("شناسه قبض:", information["bill_id"])
        print("شناسه پرداخت:", information["payment_id"])
        print("مبلغ:", information["amount"])
        print("نوع قبض:", information["type"])
    else:
        print("Invalid")