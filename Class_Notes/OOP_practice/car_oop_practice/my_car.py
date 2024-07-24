# create object/instance - my_car
# cars only, no electric

from car import Car

my_car = Car(2007, 'honda', 'element')

print("My car info:  ", end='\b'), my_car.get_description()

my_car.update_odometer(107_289)
my_car.read_odometer()

my_car.increment_odometer(4_972)
my_car.read_odometer()

my_car.update_odometer(10_000)  # can't roll back odometer
my_car.read_odometer()

my_car.reservoir()
