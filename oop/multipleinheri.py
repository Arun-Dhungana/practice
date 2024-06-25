# class Animal:
#     def __init__(self, animal):
#         self.animal = animal

#     def print_all(self):
#         print(self.animal)
#         print("ANimal")


# class Human:
#     def __init__(self, animal):
#         self.animal = animal

#     def print_all(self):
#         print(self.animal)
#         print("Human")


# class Cow(Animal, Human):
#     def __init__(self, animal, any):
#         self.value = animal

#         super().__init__(animal)

#         print(animal, any)


# Cow("Man", "how").print_all()


class A:
    def __init__(self):
        print("A's __init__")
        super().__init__()


class B(A):
    def __init__(self):
        print("B's __init__")
        super().__init__()


class C(A):
    def __init__(self):
        print("C's __init__")
        # super().__init__()


class D(B, C):
    def __init__(self):

        super().__init__()
        print("D's __init__")


d = D()
