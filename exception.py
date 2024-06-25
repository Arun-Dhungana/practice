class Adultxception(Exception):
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_minor(self):
        if self.age >= 18:
            raise Adultxception
        else:
            return self.age

    def display(self):
        try:
            print(f"age--> {self.get_minor()}")
        except Adultxception:
            print("Person is an adult")
        finally:
            print(f"Name-->{self.name}")


Person("Ram", 18).display()
