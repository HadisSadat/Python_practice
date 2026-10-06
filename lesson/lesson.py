class Lesson:

    def __init__(self):
        self.code = None
        self.name = None
        self.teacher = None

    def save(self):
        print(f"Saved : {self.code} {self.name} {self.teacher}")

    def edit(self):
        print("Edited")

    def __repr__(self):
        return f"{self.code} {self.name} {self.teacher}"