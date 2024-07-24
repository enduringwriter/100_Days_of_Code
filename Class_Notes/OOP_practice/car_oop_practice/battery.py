"""a class without inheritance"""


class Battery:
    """Model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def size_of_battery(self):
        """Display a statement describing the battery size."""
        print(f"This car has a {str(self.battery_size)} kWh battery.")

    def get_range(self):
        """Display a statement about the range this battery provides."""
        range_of_battery = 0
        if self.battery_size == 70:
            range_of_battery = 350
        elif self.battery_size == 85:
            range_of_battery = 400
        print(f"This car can go approximately {range_of_battery} miles on a full charge.")

    def upgrade_battery(self):
        """Determine if the customer would like to upgrade the battery."""
        if self.battery_size == 70:
            upgrade = input(f"Would you like to upgrade your electric car battery from {self.battery_size} to 85 kWh?"
                            " Enter 'y' for Yes or 'n' for No.").lower()
            if upgrade == 'y':
                print("Your vehicle's battery has been upgraded!")
                self.battery_size = 85
            else:
                print("Your vehicle's battery has not been upgraded.")
        else:
            print("Your vehicle already has the upgraded battery size.")
