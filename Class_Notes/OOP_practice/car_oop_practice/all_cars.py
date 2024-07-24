# cars, hybrids, and electric cars

from car import Car
from electric_car import ElectricCar

# my_car2
my_car2 = Car(2026, 'Toyota', "Camry")
print("My car info:  ", end='\b'), my_car2.get_description()

my_car2.update_odometer(7_289)
my_car2.read_odometer()

my_car2.update_odometer(1_000)  # can't roll back odometer
my_car2.read_odometer()

my_car2.reservoir()

# my_electric_car2
print('\n')
my_electric_car2 = ElectricCar(2026, 'Honda', "CR-V")
print("My car info:  ", end='\b'), my_electric_car2.get_description()

my_electric_car2.update_odometer(9_789)
my_electric_car2.read_odometer()

my_electric_car2.update_odometer(1_000)  # can't roll back odometer
my_electric_car2.read_odometer()

my_electric_car2.reservoir()

print('\n')
my_electric_car2.battery.upgrade_battery()
my_electric_car2.battery.get_range()
