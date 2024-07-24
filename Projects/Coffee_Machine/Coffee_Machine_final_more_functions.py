# Coffee Machine Project
# water and milk are in ml
# coffee is in grams

from data import menu, resources

# global variables
global water_required, milk_required, coffee_required, cost, can_brew_coffee


def cost_of_coffee(selection):
    """Input type of coffee user selected and return the cost of that coffee."""
    global cost
    if selection == "espresso":
        cost = menu["espresso"]["cost"]
    elif selection == "latte":
        cost = menu["latte"]["cost"]
    elif selection == "cappuccino":
        cost = menu["cappuccino"]["cost"]
    return cost


def process_tender():
    """Returns total monies that customer has tendered."""
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    tender = quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01
    return tender


def resources_required(selection):
    """return requirements to brew a selected coffee, by getting data from data.py."""
    global water_required, milk_required, coffee_required
    if selection == "espresso":
        water_required = menu["espresso"]["ingredients"]["water"]
        milk_required = 0
        coffee_required = menu["espresso"]["ingredients"]["coffee"]
    elif selection == "latte":
        water_required = menu["latte"]["ingredients"]["water"]
        milk_required = menu["latte"]["ingredients"]["milk"]
        coffee_required = menu["latte"]["ingredients"]["coffee"]
    elif selection == "cappuccino":
        water_required = menu["cappuccino"]["ingredients"]["water"]
        milk_required = menu["cappuccino"]["ingredients"]["milk"]
        coffee_required = menu["cappuccino"]["ingredients"]["coffee"]
    return water_required, milk_required, coffee_required


def resources_update_and_return_status(selection, water, milk, coffee):
    """return current status of resources."""
    global water_required, milk_required, coffee_required
    water_required, milk_required, coffee_required = resources_required(selection)  # call function resources required
    water -= water_required
    milk -= milk_required
    coffee -= coffee_required
    return water, milk, coffee


def check_resources_to_brew_coffee(selection, water, milk, coffee):
    """Return True when the order can be brewed, False if resources are insufficient.
    Also return shortages of items, if any."""
    shortage = []
    global can_brew_coffee, water_required, milk_required, coffee_required
    water_required, milk_required, coffee_required = resources_required(selection)  # call function resources required
    if water >= water_required and milk >= milk_required and coffee >= coffee_required:
        can_brew_coffee = True
    else:
        if water <= water_required:
            can_brew_coffee = False
            shortage.append("water")
        if milk <= milk_required:
            can_brew_coffee = False
            shortage.append("milk")
        if coffee <= coffee_required:
            can_brew_coffee = False
            shortage.append("coffee")
    return can_brew_coffee, shortage


def coffee_machine():
    """Coffee machine brews 3 types of coffees: espresso, latte, and cappuccino.
    It is coin operated and accepts US coins: quarters, dimes, nickels, and pennies.
    Type 'report' to view water, milk, and coffee levels, as well as how much money
    the coffee machine has accumulated. Type 'off' to power off the coffee machine."""

    power_on = True

    # initial resources to start with
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    # variables
    money_cumulative = 0

    # global variables
    global water_required, milk_required, coffee_required, cost, can_brew_coffee

    while power_on:
        selection = input("\tWhat would you like? (espresso/latte/cappuccino): ")

        if selection == "report":
            print(f"Water: {water}ml\nMilk: {milk}ml\ncoffee: {coffee}g\nMoney: ${money_cumulative:.2f}")

        elif selection == "espresso" or selection == "latte" or selection == "cappuccino":

            # call function to check if can't brew and list shortages
            can_brew_coffee, shortage = check_resources_to_brew_coffee(selection, water, milk, coffee)

            # call function to get the cost of coffee that the user selected
            transaction_cost = cost_of_coffee(selection)

            # call function to get total monies tendered by customer
            tender = process_tender()

            # complete transaction and refund_amount, if any
            if tender < transaction_cost:
                print(f"Sorry that's not enough money. Money refunded: ${tender:.2f}")
            elif not can_brew_coffee:
                print(f"Sorry there is not enough {shortage}.")
            elif tender >= transaction_cost:
                refund = round((tender - transaction_cost), 2)
                print(f"Here is ${refund:.2f} in change.")
                print(f"Here is your {selection} ☕.️ Enjoy!")

            # call function to update resources if a purchase is made, and return current resources
            if (selection == "espresso" or "latte" or "cappuccino") and (
                    tender >= transaction_cost) and can_brew_coffee:

                # call function to get resources required to brew
                water, milk, coffee = resources_update_and_return_status(selection, water, milk, coffee)

                # Cumulative purchases that the coffee machine generates
                money_cumulative += round(transaction_cost, 2)

        elif selection == "off":
            power_on = False


coffee_machine()
