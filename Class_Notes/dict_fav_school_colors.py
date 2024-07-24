# dictionary favorite school colors

from pprint import pprint

# variables
schools = {
    'Sing Fighter Academy': {'color': ['black', 'white'], 'year': 2020},
    'Enduring Writer Academy': {'color': 'cyan', 'year': 2019},
    'University of North Texas': {'color': ['white', 'green'], 'year': 2019},
    'Texas A&M University': {'color': ['white', 'maroon'], 'year': 2000},
    'Michigan State University': {'color': ['white', 'green'], 'year': 2005}}

favorite_schools = [
    'University of North Texas',
    'Texas A&M University']

school_colors_white = ['white']

# print dictionary - standard print method
print(f'Original fav_colors: {schools}\n')

# pprint "pretty print" dictionary - easier to read
pprint(f'Original fav_colors: {schools}', indent=1, width=80, compact=False, sort_dicts=True)  # underscore_numbers=True
print('\n')

# for loop print dictionary - easiest to read
for k, v in schools.items():
    print(k, v)
print('\n')


def fav_schools_sorted(school_list, fav_schools):
    """
    Favorite schools alphabetized
    :param school_list: list of schools
    :param fav_schools: identify favorite schools
    :return:
    """
    for school in sorted(school_list.keys()):  # sort fav schools
        if school in fav_schools:
            print(f"Favorite School: {school}")


def school_colors_with_white(school_list, check_color):
    """
    List all schools that have white as one of the school's color
    :param school_list: list of schools and their school colors
    :param check_color: identify schools that have the specified color in their school colors
    :return: school colors that have the specified color as a school color
    """
    for school in school_list.values():
        for color in school["color"]:
            if color in check_color:
                print(f"School colors that have {check_color}: {school['color']}")


def schools_with_white_school_color(school_list, check_color):
    """
    list all schools and their colors, if white is one of the school's colors
    :param school_list: list of schools and their school colors
    :param check_color: identify schools that have the specified color in their school colors
    :return: schools and their school colors that have the specified color as a school color
    """
    for school, values in school_list.items():
        for color in values["color"]:
            if color in check_color:
                print(f"Schools and their colors, if one of the colors includes"
                      f" {''.join(check_color)}: {school}: {', '.join(values['color']).rjust(20)}")


fav_schools_sorted(schools, favorite_schools)
print('\n')
school_colors_with_white(schools, school_colors_white)
print('\n')
schools_with_white_school_color(schools, school_colors_white)
print('\n')
