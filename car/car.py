class Car:

    def __init__(self,name, color, plate):
        self.name = name
        self.color = color
        self.plate = plate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value,str):
            raise TypeError("name must be string")
        self.__name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be string")
        self.__color = value

    @property
    def plate(self):
        return self.__plate

    @plate.setter
    def plate(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be string")
        self.__plate = value

    def __repr__(self):
        return f"{self.name} {self.color} {self.plate}"