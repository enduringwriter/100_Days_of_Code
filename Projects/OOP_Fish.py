# OOP Classes practice Day 21

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale.")

# NO INHERITANCE
# class Fish:
#     def swim(self):
#         print("Moving in water")
#
# nemo = Fish()


# INHERITANCE FROM THE ANIMAL CLASS
class Fish(Animal):  # the class Fish is inheriting from Animal class
    def __init__(self):
        # superclass allows all methods and attributes of the Animal class to be applied to the Fish class
        super().__init__()  # super() calls the Animal class and then calls the initializer
        # super() is not required, but is recommended

    def breath(self):
        super().breath()  # calling Animal class method breathe()
        print("Doing this underwater.")

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)
