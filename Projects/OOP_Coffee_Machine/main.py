# OOP Coffee Machine
# Learn to create objects from classes and to use modules and attributes that belong to those classes.
# Import the teacher's preexisting data files which have classes, modules, and attributes.
# This project demonstrates object-oriented programming "OOP" of a coffee machine

# import 3 files that contain 4 Classes
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    power_on = True

    # create objects from Classes
    menu = Menu()
    # menu_item = MenuItem()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while power_on:

        # Menu() has module get_items() to display all available menu items
        choice = input(f"What would you like? {menu.get_items()}: ")

        if choice == "off":
            power_on = False

        elif choice == "report":
            # CoffeeMaker() has module report() to print current resources
            # MoneyMachine() has module report() to print current profit
            # print both reports
            coffee_maker.report()
            money_machine.report()

        elif choice in menu.get_items():
            # create object drink and link it to user's choice, if user's choice is in the menu
            drink = menu.find_drink(choice)

            #  check if the coffee machine has sufficient resources to brew customer's order
            if coffee_maker.is_resource_sufficient(drink):
                print("yes")

                # check if customer tender is sufficient, if so process payment and refund change, if any
                if money_machine.make_payment(drink.cost):

                    # brew coffee for customer and update resources
                    coffee_maker.make_coffee(drink)


coffee_machine()
