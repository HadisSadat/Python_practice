from personal_module import *


while True:
    option = show_menu()
    print("------------------------------------")

    match option:
        case 1:
            check_national_id()


        case 2:
            check_phone_number()


        case 3:
            check_card_number()

        case 4:
            check_plate_number()

        case 5:
            check_bill_id()

        case 0:
            print("Exit")
            break

        case _:
            print("Invalid Option")
    print("------------------------------------")