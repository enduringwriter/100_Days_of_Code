import json  # not required is using native .write() and .read() with .json files


def get_stored_username():
    """Get stored username if available."""
    filename = "username.json"
    try:
        with open(filename) as file:
            username = file.readlines()
    except FileNotFoundError:
        return None
    else:
        # print(user)
        return username


# get_stored_username()


def get_new_username():
    """Prompt for a new username."""
    username = input("Please enter your username: ")
    filename = "username.json"
    with open(filename, "w") as file:
        json.dump(username, file)
        # file.write(username)  # works with json files and don't need to import json
        print(f"We'll remember you when you come back {username}!")


def greet_user():
    """Greet user by username."""
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}")
    else:
        get_new_username()


greet_user()
