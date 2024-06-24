class Animal:
    def __init__(self):
        self.animal = "Cow"


class Cow(Animal):
    def __init__(self):
        self.value = ""
        super().__init__()
