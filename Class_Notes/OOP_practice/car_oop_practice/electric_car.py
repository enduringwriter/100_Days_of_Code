"""A child class that inherits the parent class"""

from car import Car
from battery import Battery


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, year, make, model):
        """Initialize attributes of the parent class."""
        super().__init__(year, make, model)
        # create a new instance of the Battery class and store it in the attribute self.battery
        self.battery = Battery()  # call the battery class by assigning it to the parameter

    # override reservoir parent class for all instances in child class ElectricCar fully b/c these don't use gas
    def reservoir(self):
        return print("This car doesn't need a gas tank.")
