# fav pizza and toppings
# arbitrary number of arguments passed to a function


def make_pizza(size, *toppings):
    """
    Summarize the pizza to make.
    :param size: size of pizza - small = 8, medium = 12, large = 16
    :param toppings: pizza toppings i.e. pepporoni and black olives
    :return: pizza size and toppings
    """
    print(f"Making a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(12, 'pepperoni')
make_pizza(16, 'pepperoni', 'mushrooms', 'black_olives', 'extra_cheese', 'extra_sauce')
