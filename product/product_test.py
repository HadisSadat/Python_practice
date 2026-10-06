from product import Furniture, Laptop, Iphone, Samsung

sofa = Furniture("3 seater", "Dark Blue")
sofa.name = "Royal Sofa"
sofa.price = "$850"
sofa.weight = "45 kg"
print(sofa)

laptop = Laptop("8.00 GB", "Intel Core i5")
laptop.name = "ASUS ZenBook"
laptop.price = "$750"
laptop.voltage = "19V"
print(laptop)

mobile = Iphone("13 normal")
mobile.name = "iphone"
mobile.price = "$599"
mobile.voltage = "3.83V"
mobile.size = "6.1 inches"
print(mobile)

mobile_ = Samsung("Galaxy A55")
mobile_.name = "samsung"
mobile_.price = "$450"
mobile_.voltage = "3.87V"
mobile_.size = "6.6 inches"
print(mobile_)