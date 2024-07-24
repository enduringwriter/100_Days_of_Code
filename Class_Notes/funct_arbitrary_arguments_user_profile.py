# user profiles
# optional argument passed to a function - middle name
# arbitrary arguments passed to a function - additional user info


def build_profile(first, last, middle='', **user_info):
    """
    Build a dictionary containing everything known about a user.
    :param first: user's first name
    :param middle: user's middle name
    :param last: user's last name
    :param user_info: other unknown information to be added to user profile
    :return: user profile
    """
    profile = {'first': first, 'middle': middle, 'last': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(first='keith',
                             last='stateson',
                             location='Texas',
                             field=['chemistry', 'music', 'business', 'creative writing', 'data science'])

print(user_profile)
