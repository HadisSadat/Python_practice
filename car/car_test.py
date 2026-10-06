from car import Car

car_1 = Car()
car_1.name  = "BMW"
car_1.color = "black"
car_1.plate = "62D72855"
car_1.save()
car_1.change_plate()
print(car_1)