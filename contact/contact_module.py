contact_list = []

def contact_menu():
    print("1)add contact")
    print("2)contact list")
    print("3)search by phone")
    print("0)Exit")
    option = int(input("Enter an option :"))
    return option

def contact_info():
    name = input("Enter a name : ")
    last_name = input("Enter a last name : ")
    number = int(input("Enter a number : "))
    title = input("Enter a title : ")
    return {"name":name, "last name":last_name, "number":number, "title":title}

def print_contact(contact_list):
    for person in contact_list:
        print(f"{person['name']:10} {person['last name']:10} {person['number']:10} {person['title']}:10")

def search_contact(contact_list, number):
    for person in contact_list:
        if person['number'] == number :
            return person