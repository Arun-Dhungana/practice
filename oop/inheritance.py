class Animal:
    def __init__(self, animal):
        self.animal = animal

    def print_all(self):
        print(self.animal)


class Cow(Animal):
    def __init__(self, animal):
        self.value = animal
        super().__init__(animal)

    def print_all(self):
        print("Hello")


Cow("Man").print_all()
