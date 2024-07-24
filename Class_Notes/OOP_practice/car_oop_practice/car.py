"""A class that is used to represent a car."""


class Car:
    """Car information."""
    def __init__(self, year, make, model):
        """
        Initialize attributes to describe a car.
        :param year: Year car was manufactured
        :param make: Manufacturer
        :param model: Model of car
        """
        self.year = year
        self.make = make
        self.model = model
        self.odometer_reading = 0
        self.tank_size = 16

    def get_description(self):
        """Return a neatly formatted descriptive name - year make model."""
        long_name = f"{self.year} {self.make} {self.model} {self.odometer_reading:,}"
        return print(long_name.title() + " miles on it.")

    def reservoir(self):
        """Return reservoir of gas tank in gallons."""
        return print(f"This vehicle has a {self.tank_size} gallon reservoir.")

    def read_odometer(self):
        """Display the vehicle's mileage."""
        print(f"This vehicle has {self.odometer_reading:,} miles on it.")  # ':,' displays number separated with comma

    def update_odometer(self, mileage):
        """Update the vehicle's mileage."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount of miles to the odometer reading."""
        self.odometer_reading += miles
