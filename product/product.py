class Product:
    def __init__(self):
        self.name = None
        self.price = None

class NonElectric(Product):
    def __init__(self):
        self.weight = None

class Electric(Product):
    def __init__(self):
        self.voltage = None

class Furniture(NonElectric):
    def __init__(self, seater, color):
        self.seater = seater
        self.color = color

    def __repr__(self):
        return (f"{self.name} "
                f"{self.price} "
                f"{self.weight} "
                f"{self.seater} "
                f"{self.color}")

class Mobile(Electric):
    def __init__(self):
        self.size = None

class Laptop(Electric):
    def __init__(self, ram, cpu):
        self.ram = ram
        self.cpu = cpu

    def __repr__(self):
        return (f"{self.name} "
                f"{self.price} "
                f"{self.voltage} "
                f"{self.ram} "
                f"{self.cpu}")

class Iphone(Mobile):
    def __init__(self, series):
        self.series = series

    def __repr__(self):
        return (f"{self.name} "
                f"{self.price} "
                f"{self.voltage} "
                f"{self.size}"
                f"{self.series}")

class Samsung(Mobile):
    def __init__(self, series):
        self.series = series

    def __repr__(self):
        return (f"{self.name} "
                f"{self.price} "
                f"{self.voltage} "
                f"{self.size}"
                f"{self.series}")