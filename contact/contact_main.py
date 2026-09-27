from module import *

while True:
    option = contact_menu()
    print("<><><><><><><><><><><><><><><><><><><><><>")

    match option:
        case 1:
            person = contact_info()
            if search_contact(contact_list,person['number']):
                print("exist")
            else:
                contact_list.append(person)

        case 2:
            print_contact(contact_list)

        case 3:
            number = int(input("Enter a number : "))
            result = search_contact(contact_list,number)
            if result:
                print("found")
            else:
                print("not found")

        case 0:
            break

        case _:
            print("invalid information")

    print("<><><><><><><><><><><><><><><><><><><><><>")