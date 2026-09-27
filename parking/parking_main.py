from parking_module import *

while True:
    option = parking_menu()
    print("____________________________________")

    match option:
        case 1:
            get_info = parking_info()
            if parking_search(parking_list, get_info["plate"]):
                print("car already exists")
            else:
                parking_list.append(get_info)

        case 2:
            parking_list_print(parking_list)

        case 3:
            plate = input("Enter a plate : ")
            result = parking_search(parking_list, plate)
            if result:
                print("found ", result)
            else:
                print("not found")

        case 0:
            break

        case _:
            print("invalid information")

    print("____________________________________")