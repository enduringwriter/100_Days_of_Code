# ordering a dictionary using OrderedDict() in module collections
# OrderedDict() - dict subclass that remembers the order entries were added

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'fortran'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
