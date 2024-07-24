# create object/instance - my_electric_car
# electric cars only, no gas cars and no hybrids

from electric_car import ElectricCar  # child class automatically includes import of parent class

my_electric_car = ElectricCar(2024, 'Kia', 'excel')

my_electric_car.update_odometer(12_538)

print("My electric car info:  ", end='\b'), my_electric_car.get_description()

my_electric_car.reservoir()
my_electric_car.battery.size_of_battery()
my_electric_car.battery.get_range()

print('\n'), my_electric_car.battery.upgrade_battery(), my_electric_car.battery.get_range()
