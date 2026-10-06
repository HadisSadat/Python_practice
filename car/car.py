class Car:

    def __init__(self):
        self.name = None
        self.color = None
        self.plate = None

    def save(self):
        print(f"Saved : {self.name} {self.color} {self.plate}")

    def change_plate(self):
          print("Change Plate")

    def __repr__(self):
        return f"{self.name} {self.color} {self.plate}"