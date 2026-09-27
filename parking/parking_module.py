parking_list = []


def parking_menu():
    print("1)Enter to parking")
    print("2)parking list")
    print("3)search car by plate")
    print("0)Exit")
    option = int(input("Enter an option : "))
    return option


def parking_info():
    name = input("Enter a name : ")
    color = input("Enter a color : ")
    plate = input("Enter a plate : ")
    time = input("Enter a time : ")
    return {"name": name, "color": color, "plate": plate, "time": time}


def parking_search(parking_list, plate):
    for car in parking_list:
        if car["plate"] == plate:
            return car


def parking_list_print(parking_list):
    for car in parking_list:
        print(f"{car['name']:10} {car['color']:10} {car['plate']:10} {car['time']:10}")