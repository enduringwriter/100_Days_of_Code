# practice

# create Class
class Vegetable:
    pass  # pass statement is used as a placeholder for future code and prevents python debugger error


def xyz():
    pass  # another example of pass, which prevents the debugger error as python expects code in a function or class


# create object
veggie_1 = Vegetable()
veggie_2 = Vegetable()

# attributes are variables associated with an object

# create veggie 1
veggie_1.id = "001"
veggie_1.name = "apple"

# create veggie 2
veggie_2.id = "002"
veggie_2.name = "banana"

print(veggie_1.name)
print(veggie_2.name)


class Car:

    def __init__(self, seats):
        self.seats = seats


# car = Car()
car_1 = Car(5)

car_2 = Car(None)
car_2.seats = 4

car_3 = Car(0)
car_3.seats = 6

# print(car.seats)
print(f"car_1 has {car_1.seats} seats")
print(f"car_2 has {car_2.seats} seats")
print(f"car_3 has {car_3.seats} seats")

# https://www.scaler.com/topics/constructor-in-python/
# constructor is created by the programmer or else Python will automatically generate the default constructor
# 3 types: Parameterized Constructor, Non-Parameterized Constructor, Default Constructor
