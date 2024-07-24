# create class called "User" of customer users
class User:

    # create a constructor method
    # a constructor is a method that is called when an object is created of a class i.e. user_1 = User()
    # a method, unlike a function, requires a self parameter
    # create attributes i.e. id, username, followers, following
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # the attributes are the things the object has
    # methods are the things the object does

    # create a method called "follow"
    def follow(self, user):
        """ follow method increases follow/following counts when a user decides to follow another user
        """
        user.followers =+ 1  # count of the user who is being followed goes up by one
        self.following += 1  # one's own following count goes up by one

#  create objects from class User()
user_1 = User("001", "keith")
user_2 = User("002", "jane")
user_3 = User(None, None)

user_3.id = "003"

# print(user_1.id)
# print(user_2.id)
# print(user_3.id)

user_1.follow(user_2)

print(f"{user_1.username}'s followers: {user_1.followers}")
print(f"{user_1.username}'s following: {user_1.following}")
print(f"{user_2.username}'s followers: {user_2.followers}")
print(f"{user_2.username}'s following: {user_2.following}")
print(f"{user_3.username}'s followers: {user_3.followers}")
print(f"{user_3.username}'s following: {user_3.followers}")

# # create user list
# user_list = []
# print(user_list)  # prints empty list
#
# # append instances to user list
# user_list.append(User("101", "ABC"))
# user_list.append(User("102", "DEF"))
# user_list.append(User("103", "GHI"))
#
# print(user_list)  # prints brackets of list, but then prints memory location of objects
#
# # print user list attributes
# for user in user_list:
#     print(f"ID: {user.id}, Username: {user.username}, Followers: {user.followers}")
