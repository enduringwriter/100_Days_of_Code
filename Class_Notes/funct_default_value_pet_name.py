# pet name
# default value within a function


def describe_pet(pet_name, animal_type='dog'):
    """
    Display information about a pet.
    :param pet_name: Name of pet
    :param animal_type: Type of animal
    :return: Type and name of animal
    """
    print(f"{animal_type.title()}'s name is {pet_name}")


describe_pet("max")
